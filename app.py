from flask import Flask, render_template, request, jsonify, send_file
import json
from pathlib import Path
import importlib.util
import copy
from datetime import datetime

app = Flask(__name__)
PROBLEM = Path(__file__).parent / 'problems'
SUBMISSION = Path(__file__).parent / 'outputs'
SUBMISSION.mkdir(exist_ok=True)
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

def get_shortest_submission(task):
    subs = SUBMISSION / task
    if not subs.exists():
        return None
    py_files = list(subs.glob("*.py"))
    if not py_files:
        return None
    return min(py_files, key=lambda x: int(x.stem.split('_')[0]))  # shortest submission

@app.route('/')
def index():
    tasks_info = []
    overall_score = 0
    for i, task in enumerate(task_names):
        shortest_sub = get_shortest_submission(task)
        if shortest_sub:
            exists = True
            code = shortest_sub.stat().st_size
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
    shortest_sub = get_shortest_submission(task)
    code = shortest_sub.read_text() if shortest_sub else ""
    hints = collect_hints(problems[task])
    return render_template('problem.html', task=task, problem=problems[task], code=code, hints=hints, summary=summaries[task_names.index(task)][0], hardness=summaries[task_names.index(task)][1])

@app.post('/submit')
def submit():
    data = request.json
    task: str = data["task"]
    code: str = data["code"]
    code = code.strip()
    code = code.replace("\r\n", "\n")  # Normalize line endings
    if task not in problems:
        return jsonify({
            "success": False,
            "error_type": "task_not_found",
            "error_message": "Task not found",
        }), 404
    old_code = get_shortest_submission(task).read_text() if get_shortest_submission(task) else None

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
            if output != expected_output:
                mismatch.append({
                    "index": i,
                    "output": output,
                })
    except Exception as e:
        return jsonify({
            "success": False,
            "error_type": "execution",
            "error_message": str(e),
        })
    if len(mismatch) > 0:
        return jsonify({
            "success": False,
            "error_type": "test",
            "mismatch": mismatch,
        })
    
    # everything is fine, save the submission
    (SUBMISSION / task).mkdir(exist_ok=True)
    new_sub = SUBMISSION / task / f"{len(code):03d}_{datetime.now().strftime('%Y%m%d%H%M%S')}.py"
    new_sub.write_bytes(code.encode("utf-8"))
    return jsonify({"success": True, "size": len(code), "score": max(1, 2500 - len(code)), "shortest": old_code is None or len(code) < len(old_code)})

@app.route('/download')
def download():
    import zipfile
    from io import BytesIO

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for task in task_names:
            if (shortest_sub := get_shortest_submission(task)) is not None:
                zip_file.write(shortest_sub, arcname=f"{task}.py")

    zip_buffer.seek(0)
    return send_file(zip_buffer, as_attachment=True, download_name='submission.zip', mimetype='application/zip')