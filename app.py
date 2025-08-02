from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)
PROBLEM = Path(__file__).parent / 'problems'
SUBMISSION = Path(__file__).parent / 'outputs'

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

@app.route('/problem/<task>')
def problem(task):
    if task not in problems:
        return jsonify({"error": "Task not found"}), 404
    sub = SUBMISSION / f"{task}.py"
    if sub.exists():
        code = sub.read_text()
    else:
        code = ""
    return render_template('problem.html', task=task, problem=problems[task], code=code)
