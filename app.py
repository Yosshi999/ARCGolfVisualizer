from flask import Flask, render_template, request, jsonify, send_file
import json
from pathlib import Path
import importlib.util
import copy
from datetime import datetime
import traceback
import sys
import re
import numpy
from get_global_shortest import get_global_shortests

app = Flask(__name__)
PROBLEM = Path(__file__).parent / 'problems'
SUBMISSION = Path(__file__).parent / 'outputs'
SUBMISSION.mkdir(exist_ok=True)

# Cache management
global_shortest_cache = {}
cache_file = Path("global_shortest_cache.json")

def load_cache():
    """Load cache from file on startup"""
    if cache_file.exists():
        return json.loads(cache_file.read_text())
    return {}

def save_cache(data):
    """Save cache to file"""
    cache_file.write_text(json.dumps(data, indent=2))

def get_cached_global_shortest():
    """Get cached global shortest data"""
    return global_shortest_cache

def sync_global_shortest_data():
    """Sync global shortest data from Google Sheets"""
    fresh_data = get_global_shortests()
    global_shortest_cache.update(fresh_data)
    save_cache(global_shortest_cache)
    return fresh_data

# Load cache on startup
global_shortest_cache = load_cache()
summaries = []
for line in Path("claude_summary.tsv").read_text(encoding="utf-8").strip().split("\n")[1:]:
    func, hardness = line.split("\t")
    summaries.append((func, int(hardness)))

problems = {}
for p in sorted(PROBLEM.glob('*.json')):
    with open(p, 'r') as f:
        data = json.load(f)
        problems[p.stem] = data["train"] + data["test"] + data["arc-gen"]

task_names = list(problems.keys())
print(f"found tasks: {len(task_names)}")
assert len(task_names) == len(summaries), "Number of tasks does not match number of summaries."

def get_local_shortest_submission(task: str):
    subs = SUBMISSION / task
    if not subs.exists():
        return None
    py_files = list(subs.glob("*.py"))
    if not py_files:
        return None
    return min(py_files, key=lambda fn: len(normalize_code(fn.read_text(encoding="utf-8"))))  # shortest submission

def normalize_code(code: str) -> str:
    return code.strip().replace("\r\n", "\n")

@app.route('/')
def index():
    tasks_info = []
    overall_score = 0
    global_shortest_bytes = get_cached_global_shortest()
    for i, task in enumerate(task_names):
        shortest_sub = get_local_shortest_submission(task)
        if shortest_sub:
            exists = True
            code = len(normalize_code(shortest_sub.read_text()))
            score = max(1, 2500 - code)
        else:
            exists = False
            code = 0
            score = 0
        tasks_info.append({
            "name": task,
            "exists": exists,
            "summary": summaries[i][0],
            "hardness": summaries[i][1],
            "global_shortest": global_shortest_bytes.get(task, float('inf')),
            "size": code,
            "score": score,
        })
        overall_score += score
    # Sort tasks based on the query parameter
    sort_by = request.args.get('sort', 'name')
    other = "score" if sort_by == "hardness" else "hardness"
    tasks_info.sort(key=lambda v: (v[sort_by], v[other]))
    return render_template('index.html', tasks_info=tasks_info, overall_score=overall_score)

def collect_hints(problem):
    hints = []
    # all input has same dimensions
    in_dimensions = set()
    for p in problem:
        in_dimensions.add((len(p["input"]), len(p["input"][0])))
    if len(in_dimensions) == 1:
        in_dim = in_dimensions.pop()
        hints.append(f"All inputs have the same dimensions: {in_dim[0]}x{in_dim[1]}")
    # all output has same dimensions
    out_dimensions = set()
    for p in problem:
        out_dimensions.add((len(p["output"]), len(p["output"][0])))
    if len(out_dimensions) == 1:
        out_dim = out_dimensions.pop()
        hints.append(f"All outputs have the same dimensions: {out_dim[0]}x{out_dim[1]}")
    return hints

@app.route('/problem/<task>')
def problem(task):
    if task not in problems:
        return jsonify({"error": "Task not found"}), 404
    global_shortest_byte = get_cached_global_shortest().get(task, float('inf'))
    shortest_sub = get_local_shortest_submission(task)
    code = shortest_sub.read_text() if shortest_sub else ""
    hints = collect_hints(problems[task])
    return render_template('problem.html', task=task, problem=problems[task], code=code, hints=hints, summary=summaries[task_names.index(task)][0], hardness=summaries[task_names.index(task)][1], global_shortest=global_shortest_byte)

@app.post('/submit')
def submit():
    data = request.json
    task: str = data["task"]
    code: str = data["code"]
    saveFile: bool = data["saveFile"]
    code = normalize_code(code)
    if task not in problems:
        return jsonify({
            "success": False,
            "error_type": "task_not_found",
            "error_message": "Task not found",
        }), 404
    old_code = get_local_shortest_submission(task).read_text() if get_local_shortest_submission(task) else None

    mismatch = []
    try:
        task_modname = "task_with_imports"
        spec = importlib.util.spec_from_loader(task_modname, loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(code, module.__dict__)
        assert hasattr(module, "p"), "Unable to locate function p()."
        program = getattr(module, "p")
        assert callable(program), "p() is not callable."
        for i, example in enumerate(problems[task]):
            input_data = copy.deepcopy(example["input"])
            expected_output = copy.deepcopy(example["output"])
            output = program(input_data)
            
            # Convert output to proper format using JSON normalization
            try:
                result = json.dumps(output)
                result = result.replace("true", "1").replace("false", "0")
                unsafe_chars = re.compile(r"[^0-9,\[\]\s\.]")
                if unsafe_chars.search(result):
                    return jsonify({
                        "success": False,
                        "error_type": "type_error",
                        "error_message": f"Invalid output format: {result[:500]}",
                    })
                output = json.loads(result)
            except Exception as e:
                return jsonify({
                    "success": False,
                    "error_type": "type_error",
                    "error_message": f"Output format error: {str(e)}",
                })
            
            # Use numpy array comparison
            try:
                user_output = numpy.array(output)
                label_output = numpy.array(expected_output)
                if not numpy.array_equal(user_output, label_output):
                    mismatch.append({
                        "index": i,
                        "output": output,
                    })
            except Exception as e:
                return jsonify({
                    "success": False,
                    "error_type": "array_error",
                    "error_message": f"Array comparison error: {str(e)}",
                })
    except Exception as e:
        tb = traceback.extract_tb(sys.exc_info()[2])
        trace = traceback.format_list(tb)
        return jsonify({
            "success": False,
            "error_type": "execution",
            "error_message": str(e) + "\n" + "\n".join(trace),
        })
    if len(mismatch) > 0:
        return jsonify({
            "success": False,
            "error_type": "test",
            "mismatch": mismatch,
        })
    
    # everything is fine, save the submission
    if saveFile:
        (SUBMISSION / task).mkdir(exist_ok=True)
        new_sub = SUBMISSION / task / f"{len(code):03d}_{datetime.now().strftime('%Y%m%d%H%M%S')}.py"
        new_sub.write_bytes(code.encode("utf-8"))
    return jsonify({"success": True, "size": len(code), "score": max(1, 2500 - len(code)), "shortest": old_code is None or len(code) < len(old_code)})

@app.route('/download')
def download():
    import zipfile
    from io import BytesIO

    workspace = Path("submission")
    workspace.mkdir(exist_ok=True)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for task in task_names:
            if (shortest_sub := get_local_shortest_submission(task)) is not None:
                workfile = workspace / f"{task}.py"
                text = normalize_code(shortest_sub.read_text())
                workfile.write_bytes(text.encode("utf-8"))
                zip_file.write(str(workfile), arcname=f"{task}.py")

    zip_buffer.seek(0)
    return send_file(zip_buffer, as_attachment=True, download_name='submission.zip', mimetype='application/zip')

@app.route('/sync_global_shortest', methods=['POST'])
def sync_global_shortest():
    try:
        fresh_data = sync_global_shortest_data()
        return jsonify({"success": True, "count": len(fresh_data), "message": "Successfully synced shortest data"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/explorer')
def explorer():
    """Explorer page to view all tasks and their submissions."""
    tasks_data = []
    global_shortest_bytes = get_cached_global_shortest()
    
    for i, task in enumerate(task_names):
        shortest_sub = get_local_shortest_submission(task)
        
        if shortest_sub:
            local_bytes = len(normalize_code(shortest_sub.read_text()))
        else:
            local_bytes = None
        
        global_bytes = global_shortest_bytes.get(task, 9999)
        
        task_info = {
            "name": task,
            "global": global_bytes,
            "local": local_bytes,
            "hardness": summaries[i][1],
            "summary": summaries[i][0][:50] + "..." if len(summaries[i][0]) > 50 else summaries[i][0],
            "submitted": local_bytes is not None
        }
        
        if local_bytes is not None:
            task_info["delta"] = local_bytes - global_bytes
            task_info["ratio"] = local_bytes / global_bytes if global_bytes > 0 else float('inf')
        else:
            task_info["delta"] = None
            task_info["ratio"] = None
        
        tasks_data.append(task_info)
    
    return render_template('explorer.html', tasks_data=tasks_data)
