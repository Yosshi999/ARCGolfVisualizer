from flask import Flask, render_template, request, jsonify, send_file
import json
from pathlib import Path
from datetime import datetime
import urllib.parse
import re
from get_global_shortest import get_global_shortests
from comments_manager import Comment, Comments_manager
from zlib_optimizer.zip_src import zip_src

# import common judge utilities
from judge.core import normalize_code, judge_code
from judge.utils import get_local_shortest_submission, load_problems_from_dir

app = Flask(__name__)
PROBLEM = Path(__file__).parent / 'problems'
SUBMISSION = Path(__file__).parent / 'outputs'
ZLIB_SUBMISSION = Path(__file__).parent / 'compressed'
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

problems = load_problems_from_dir(PROBLEM)

task_names = list(problems.keys())
print(f"found tasks: {len(task_names)}")
assert len(task_names) == len(summaries), "Number of tasks does not match number of summaries."

comments_manager = Comments_manager()

@app.route('/')
def index():
    tasks_info = []
    overall_score = 0
    overall_best_score = 0
    global_shortest_bytes = get_cached_global_shortest()
    for i, task in enumerate(task_names):
        shortest_sub = get_local_shortest_submission(task, SUBMISSION, ZLIB_SUBMISSION)
        normal_score = max(1, 2500 - shortest_sub.normal_bytes) if shortest_sub.normal_bytes else 0
        best_score = max(1, 2500 - shortest_sub.best_bytes) if shortest_sub.best_bytes else 0

        # 上位3つのバイト数を取得し、最小値を使用
        global_shortest_list = global_shortest_bytes.get(task, [])
        global_shortest_min = min(global_shortest_list) if global_shortest_list and type(global_shortest_list) is list else float('inf')

        tasks_info.append({
            "name": task,
            "exists": shortest_sub.best_path is not None,
            "summary": summaries[i][0],
            "global_shortest_top3": global_shortest_list,
            "global_shortest": global_shortest_min,
            "normal": shortest_sub.normal_bytes,
            "best": shortest_sub.best_bytes,
            "score": normal_score,
            "diff": shortest_sub.best_bytes - global_shortest_min
        })
        overall_score += normal_score
        overall_best_score += best_score
    # Sort tasks based on the query parameter
    sort_by = request.args.get('sort', 'name')
    other = "score" if sort_by == "name" else "name"
    order = request.args.get("order", 'asc')    # デフォルトは asc
    reverse = (order == 'desc')
    tasks_info.sort(key=lambda v: (v[sort_by], v[other]), reverse=reverse)
    return render_template('index.html',
                           tasks_info=tasks_info,
                           overall_score={"normal": overall_score, "best": overall_best_score},
                           sort_by=sort_by, order=order)

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
    global_shortest_byte_top3 = get_cached_global_shortest().get(task, float('inf'))
    shortest_sub = get_local_shortest_submission(task, SUBMISSION, ZLIB_SUBMISSION)
    code = shortest_sub.normal_path.read_text()
    hints = collect_hints(problems[task])
    comments = comments_manager.get_comments(task)
    comments = sorted(comments,key=lambda c:c.id)
    return render_template(
        'problem.html',
        task=task,
        problem=problems[task],
        code=code,
        hints=hints,
        summary=summaries[task_names.index(task)][0],
        hardness=summaries[task_names.index(task)][1],
        global_shortest=global_shortest_byte_top3,
        local_shortest={"normal": shortest_sub.normal_bytes, "zlib": shortest_sub.compressed_bytes},
        comments=comments,
    )

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

    previous_shortest = get_local_shortest_submission(task, SUBMISSION, ZLIB_SUBMISSION)

    result = judge_code(task, code, problems[task])
    if not result.get("success"):
        # Return the structured result in the same shape your original endpoint used
        return jsonify(result), 400

    # everything is fine, save the submission
    if saveFile:
        (SUBMISSION / task).mkdir(exist_ok=True)
        new_sub = SUBMISSION / task / f"{len(code):03d}_{datetime.now().strftime('%Y%m%d%H%M%S')}.py"
        new_sub.write_bytes(code.encode("utf-8"))
    return jsonify({"success": True, "size": len(code), "score": max(1, 2500 - len(code)), "shortest": len(code) < previous_shortest.normal_bytes})

@app.route('/download')
def download():
    import zipfile
    from io import BytesIO

    workspace = Path("submission")
    workspace.mkdir(exist_ok=True)

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for task in task_names:
            local_shortest_path = get_local_shortest_submission(task, SUBMISSION, ZLIB_SUBMISSION).best_path
            workfile = workspace / f"{task}.py"
            text = normalize_code(local_shortest_path.read_text("L1"))
            workfile.write_bytes(text.encode("L1"))
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
        shortest_sub = get_local_shortest_submission(task, SUBMISSION, ZLIB_SUBMISSION)
        global_bytes_list = global_shortest_bytes.get(task, [])
        global_bytes_min = min(global_bytes_list) if global_bytes_list and type(global_bytes_list) is list else float('inf')
        
        task_info = {
            "name": task,
            "global_top3": global_bytes_list,
            "global": global_bytes_min,
            "local_no_zlib": shortest_sub.normal_bytes,
            "local_with_zlib": shortest_sub.best_bytes,
            "hardness": summaries[i][1],
            "summary": summaries[i][0][:50] + "..." if len(summaries[i][0]) > 50 else summaries[i][0],
            "submitted": shortest_sub.best_path is not None
        }
        
        if shortest_sub.normal_bytes is not None:
            task_info["delta_no_zlib"] = shortest_sub.normal_bytes - global_bytes_min
            task_info["ratio_no_zlib"] = shortest_sub.normal_bytes / global_bytes_min if global_bytes_min > 0 else float('inf')
        else:
            task_info["delta_no_zlib"] = None
            task_info["ratio_no_zlib"] = None

        if shortest_sub.best_bytes is not None:
            task_info["delta_with_zlib"] = shortest_sub.best_bytes - global_bytes_min
            task_info["ratio_with_zlib"] = shortest_sub.best_bytes / global_bytes_min if global_bytes_min > 0 else float('inf')
        else:
            task_info["delta_with_zlib"] = None
            task_info["ratio_with_zlib"] = None

        tasks_data.append(task_info)
    
    return render_template('explorer.html', tasks_data=tasks_data)

@app.post('/comment/<task>')
def comment(task):
    data = request.form
    comment = Comment.from_form(data=data)
    if comment.is_empty():
        return "Empty comment", 400
    comments_manager.save_comment(task,comment)
    return render_template('_comment.html',task=task,comment=comment)

@app.route('/comment/<task>/<commentid>', methods=['DELETE'])
def comment_delete(task,commentid):
    comments_manager.delete_comment(task,commentid)
    return ''

@app.route('/search/')
def searchBase():
    return render_template('search.html',query="",results=[])

@app.route('/search/<query>/')
def search(query):
    results = []
    for task in task_names:
        comments = comments_manager.get_comments(task)
        for comment in comments:
            if re.search(query,comment.text):
                results.append({
                    "taskname": task,
                    "comment": comment,
                })
    sort_by = request.args.get('sort', 'taskname')
    results.sort(key=lambda v: v[sort_by])
    return render_template('search.html',query=urllib.parse.quote(query),results=results)

@app.route("/compressed-len", methods=["POST"])
def get_compressed_len():
    data = request.json
    code = data.get("code", "")
    size = len(zip_src(code.encode()))
    return jsonify({"compressed_len": size})
