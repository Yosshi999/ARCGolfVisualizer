#!/usr/bin/env python3
import sys
import time
from pathlib import Path
from judge.utils import load_problems_from_dir, get_local_shortest_submission
from judge.core import judge_file

BASE_DIR = Path(__file__).parent
PROBLEM_DIR = BASE_DIR / 'problems'
SUBMISSION_DIR = BASE_DIR / 'outputs'

if not PROBLEM_DIR.exists():
    print("❌ Problem directory not found: expected 'problems/' with JSON files.")
    sys.exit(2)

problems = load_problems_from_dir(PROBLEM_DIR)
all_tasks = sorted(problems.keys())

failed = []

print(f"🔍 Starting validation for {len(all_tasks)} tasks...\n")

for task in all_tasks:
    path = get_local_shortest_submission(SUBMISSION_DIR, task)
    if path is None:
        failed.append((task, "No submission"))
        print(f"[FAIL] {task}: No submission found")
        continue

    start_time = time.time()
    res = judge_file(task, path, problems[task])
    elapsed_time = time.time() - start_time

    if res.get("success"):
        print(f"[OK] {task} ✅ (file={path.name}, time={elapsed_time:.2f}s)")
    else:
        error_type = res.get("error_type", "unknown")
        msg = res.get("error_message") or str(res)
        print(f"[FAIL] {task}: {error_type} → {msg[:200]} (file={path.name}, time={elapsed_time:.2f}s)")
        failed.append((task, f"{error_type}: {msg[:200]} (file={path.name}, time={elapsed_time:.2f}s)"))

print("\n===== Summary =====")
if failed:
    print(f"❌ {len(failed)} tasks failed:")
    for t, reason in failed:
        print(f"- {t}: {reason}")
    sys.exit(1)
else:
    print("✅ All tasks passed.")
    sys.exit(0)
