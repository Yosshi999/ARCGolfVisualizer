from pathlib import Path
import zipfile
from io import BytesIO

from judge.core import normalize_code, judge_code
from judge.utils import get_local_shortest_submission, load_problems_from_dir

PROBLEM = Path(__file__).parent / 'problems'
SUBMISSION = Path(__file__).parent / 'outputs'
ZLIB_SUBMISSION = Path(__file__).parent / 'compressed'

problems = load_problems_from_dir(PROBLEM)

task_names = list(problems.keys())

workspace = Path("submission")
workspace.mkdir(exist_ok=True)

score = 0
with zipfile.ZipFile("submission.zip", 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for task in task_names:
        local_shortest_path = get_local_shortest_submission(task, SUBMISSION, ZLIB_SUBMISSION).best_path
        workfile = workspace / f"{task}.py"
        text = normalize_code(local_shortest_path.read_text("L1"))
        text_bytes = text.encode("L1")
        score += max(1, 2500 - len(text_bytes))
        workfile.write_bytes(text_bytes)
        zip_file.write(str(workfile), arcname=f"{task}.py")
print("Total score:", score)