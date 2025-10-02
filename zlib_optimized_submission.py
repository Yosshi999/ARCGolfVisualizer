from pathlib import Path
import zipfile
import pandas as pd

import sys
import time
import zipfile
import warnings
warnings.simplefilter('ignore')

from zlib_optimizer.optimizer import optimize_code
from zlib_optimizer.zip_src import zip_src
from judge.utils import load_problems_from_dir, get_local_shortest_submission
from judge.core import judge_code, normalize_code


BASE_DIR = Path(__file__).parent
PROBLEM_DIR = BASE_DIR / 'problems'
SUBMISSION_DIR = BASE_DIR / 'outputs'

if not PROBLEM_DIR.exists():
    print("❌ Problem directory not found: expected 'problems/' with JSON files.")
    sys.exit(2)

problems = load_problems_from_dir(PROBLEM_DIR)
all_tasks = sorted(problems.keys())

results = []  # succeeded results
score = 0

workspace = Path("submission")
workspace.mkdir(exist_ok=True)
print(f"🔍 Starting validation for {len(all_tasks)} tasks...\n")

for task in all_tasks:
    submission_candidates = []

    print(f"--- Task: {task} ---")
    # original shortest
    path = get_local_shortest_submission(SUBMISSION_DIR, task)
    if path is None:
        print(f"[FAIL] {task} ❌ No submission found")
        continue

    code = normalize_code(path.read_text("utf-8"))
    start_time = time.time()
    res = judge_code(task, code, problems[task])
    elapsed_time = time.time() - start_time

    # plain input
    best_score = 0
    best_candidate = None
    result = None
    if res.get("success"):
        best_candidate = code.encode('L1')
        best_score = max(1, 2500 - len(code.encode('L1')))
        result = {
            "task": task,
            "file_name": path.name,
            "zlib": False,
            "unfold_renaming": False,
            "variable_renaming": False,
            "file_size": len(code.encode('L1')),
            "judge_time": elapsed_time,
        }
        print(f"[OK] {task} plain (score={best_score}, file={path.name}, time={elapsed_time:.2f}s)")
    else:
        error_type = res.get("error_type", "unknown")
        msg = res.get("error_message") or str(res)
        msg = msg.split('\n')[0][:200]
        print(f"[FAIL] {task} plain: {error_type} → {msg} (file={path.name}, time={elapsed_time:.2f}s)")

    # zlib optimized
    submission_files = (SUBMISSION_DIR / task).glob("*.py")
    for file in submission_files:
        code = normalize_code(file.read_text("utf-8"))
        for options in [
            {"unfold_renaming": True, "variable_renaming": True},
            {"unfold_renaming": True, "variable_renaming": False},
            {"unfold_renaming": False, "variable_renaming": True},
            {"unfold_renaming": False, "variable_renaming": False},
        ]:
            try:
                optimized_code: bytes = zip_src(optimize_code(code, **options).encode())

                optimized_score = max(1, 2500 - len(optimized_code))
                if optimized_score <= best_score:
                    print(f"[SKIP] {task}: No improvement (score={optimized_score}, file={file.name})", options)
                    continue

                start_time = time.time()
                res = judge_code(task, optimized_code.decode("L1"), problems[task])
                elapsed_time = time.time() - start_time

                if res.get("success"):
                    best_score = optimized_score
                    best_candidate = optimized_code
                    result = {
                        "task": task,
                        "file_name": file.name,
                        "zlib": True,
                        **options,
                        "file_size": len(optimized_code),
                        "judge_time": elapsed_time,
                    }
                    print(f"[OK] {task} zlib (score={optimized_score}, file={file.name}, time={elapsed_time:.2f}s)", options)
                else:
                    error_type = res.get("error_type", "unknown")
                    msg = res.get("error_message") or str(res)
                    msg = msg.split('\n')[0][:200]
                    print(f"[FAIL] {task} zlib: {error_type} → {msg} (file={file.name}, time={elapsed_time:.2f}s)", options)

            except Exception as e:
                print(f"[ERROR] {task} zlib: Optimization failed (file={file.name})", options)
                continue
    
    # summary
    if best_candidate is None:
        print(f"[SUMMARY] [FAIL] {task} ❌ No valid submission found")
        continue

    print(f"[SUMMARY] [OK] {task} ✅ Best submission size {len(best_candidate)} bytes")
    results.append(result)
    workfile = workspace / f"{task}.py"
    workfile.write_bytes(best_candidate)
    print(f"  Saved to {workfile}\n")
    score += max(1, 2500 - len(best_candidate))

print("\n===== Summary =====")
print(f"Total Score: {score}")

df = pd.DataFrame(results)
df.to_csv("validation_results.csv", index=False)

with zipfile.ZipFile("submissions.zip", 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for file in workspace.glob("*.py"):
        zip_file.write(file, arcname=file.name)