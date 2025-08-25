from pathlib import Path
from typing import Optional
from .core import normalize_code

# Return Path to shortest .py file under submission_dir / task
def get_local_shortest_submission(submission_dir: Path, task: str) -> Optional[Path]:
    subs = submission_dir / task
    if not subs.exists():
        return None
    py_files = list(subs.glob("*.py"))
    if not py_files:
        return None
    return min(py_files, key=lambda fn: len(normalize_code(fn.read_text(encoding="utf-8"))))

# Helper to load problems from a directory (matches original behavior)
import json

def load_problems_from_dir(problems_dir: Path):
    problems = {}
    for p in sorted(problems_dir.glob('*.json')):
        with p.open('r', encoding='utf-8') as f:
            data = json.load(f)
            problems[p.stem] = data.get("train", []) + data.get("test", []) + data.get("arc-gen", [])
    return problems
