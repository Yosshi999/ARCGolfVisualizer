from flask import Flask, render_template, request, jsonify, send_file
import json
from pathlib import Path
import importlib.util
import copy

app = Flask(__name__)
PROBLEM = Path(__file__).parent / 'problems'
SUBMISSION = Path(__file__).parent / 'outputs'
SUBMISSION.mkdir(exist_ok=True)

problems = {}
for p in sorted(PROBLEM.glob('*.json')):
    with open(p, 'r') as f:
        data = json.load(f)
        problems[p.stem] = data["train"] + data["test"] + data["arc-gen"]

task_names = list(problems.keys())
print(f"found tasks: {len(task_names)}")

@app.route('/')
def index():
    tasks_info = []
    overall_score = 0
    for task in task_names:
        sub = SUBMISSION / f"{task}.py"
        if sub.exists():
            exists = True
            with open(sub, 'rb') as f:
                code = len(f.read())
            score = max(1, 2500 - code)
        else:
            exists = False
            code = 0
            score = 0
        tasks_info.append({
            "name": task,
            "exists": exists,
            "size": code,
            "score": score,
        })
        overall_score += score
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
    sub = SUBMISSION / f"{task}.py"
    if sub.exists():
        code = sub.read_text()
    else:
        code = ""
    hints = collect_hints(problems[task])
    return render_template('problem.html', task=task, problem=problems[task], code=code, hints=hints)

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
    sub = SUBMISSION / f"{task}.py"
    if sub.exists():
        old_code = sub.read_text()
        if len(old_code) <= len(code):
            return jsonify({
                "success": False,
                "error_type": "length",
            })

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
    sub.write_bytes(code.encode("utf-8"))
    return jsonify({"success": True, "size": len(code), "score": max(1, 2500 - len(code))})

@app.route('/download')
def download():
    import zipfile
    from io import BytesIO

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for task in task_names:
            sub = SUBMISSION / f"{task}.py"
            if sub.exists():
                zip_file.write(sub, arcname=f"{task}.py")
    
    zip_buffer.seek(0)
    return send_file(zip_buffer, as_attachment=True, download_name='submission.zip', mimetype='application/zip')