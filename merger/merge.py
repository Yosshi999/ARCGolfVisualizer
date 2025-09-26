from argparse import ArgumentParser
import zipfile
import json
from pathlib import Path
import importlib.util
import copy
import zlib
import base64
import re
from judge.utils import get_local_shortest_submission

def test(problem, code) -> bool:
    try:
        task_modname = "task_with_imports"
        spec = importlib.util.spec_from_loader(task_modname, loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(code, module.__dict__)
        assert hasattr(module, "p"), "Unable to locate function p()."
        program = getattr(module, "p")
        assert callable(program), "p() is not callable."
        for i, example in enumerate(problem):
            input_data = copy.deepcopy(example["input"])
            expected_output = copy.deepcopy(example["output"])
            output = program(input_data)
            if output != expected_output:
                return False
    except Exception as e:
        print(f"Error during execution: {e}")
        return False
    return True

parser = ArgumentParser()
parser.add_argument("zip", type=str, help="Path to submissions.zip")
parser.add_argument("comment", type=str, help="Short comment for the merge")
args = parser.parse_args()

REPO = Path(__file__).absolute().parent
PROBLEM = REPO / 'problems'
SUBMISSION = REPO / 'outputs'
COMPRESSED = REPO / 'compressed'
problems = {}
for p in sorted(PROBLEM.glob('*.json')):
    with open(p, 'r') as f:
        data = json.load(f)
        problems[p.stem] = data["train"] + data["test"] + data["arc-gen"]
print(f"found tasks: {len(problems)}")

def normalize_code(code: str) -> str:
    return code.strip().replace("\r\n", "\n")

def get_local_shortest_bytes(task: str):
    sub = get_local_shortest_submission(SUBMISSION, task, encoding='L1')
    if sub is None:
        return float('inf')
    return len(sub.read_text(encoding='L1'))

def get_local_shortest_compressed_bytes(task: str):
    sub = get_local_shortest_submission(COMPRESSED, task, encoding='L1')
    if sub is None:
        return float('inf')
    return len(sub.read_text(encoding='L1'))

def is_zlib_code(code: str) -> bool:
    return code.startswith("#coding:L1")

def decode_zlib(code: str) -> str:
    m = re.search(r'zlib\.decompress\(.*\)', code, re.S)
    if not m:
        raise ValueError("Unable to find zlib.decompress(...) expression")
    expr = m.group(0)

    # 右から2個目の ')' の位置を探す
    idx = [i for i, c in enumerate(expr) if c == ')']
    if len(idx) < 1:
        raise ValueError("No closing parenthesis found in expression")
    cut = idx[-1]   # exec(...) の ')'
    if len(idx) >= 2:
        cut = idx[-2]  # zlib.decompress(...) の ')'
    expr = expr[:cut+1]

    # zlib と bytes だけを許可して評価
    data = eval(expr, {"zlib": zlib, "bytes": bytes})
    return data.decode("L1")

with zipfile.ZipFile(args.zip, 'r') as zip_ref:
    for name in zip_ref.namelist():
        if name.endswith('.py'):
            with zip_ref.open(name) as f:
                task_name = name.split("/")[-1].split(".")[0]
                code = normalize_code(f.read().decode('L1'))
                print(f"Processing {task_name}...")

                if not task_name in problems:
                    print(f"> Skipped. Task {task_name} not found in problems.")
                    continue

                if not is_zlib_code(code):
                    # normal case
                    if get_local_shortest_bytes(task_name) <= len(code):
                        print(f"> Skipped. Local shortest submission is shorter.")
                        continue
                    if test(problems[task_name], code):
                        print(f"> Passed. size: {len(code)}")
                        SUBS = SUBMISSION / task_name
                        SUBS.mkdir(exist_ok=True)
                        (SUBS / f"{len(code):03d}_{args.comment}.py").write_bytes(code.encode("L1"))
                else:
                    # zlib case
                    try:
                        plain_code = decode_zlib(code)
                    except Exception as e:
                        print(f"> Skipped. zlib decode failed: {e}")
                        continue
                    plain_len = len(plain_code)
                    comp_len = len(code)

                    out_best = get_local_shortest_bytes(task_name)
                    comp_best = get_local_shortest_compressed_bytes(task_name)

                    ok = False
                    if plain_len <= out_best:
                        ok = True
                    elif comp_len <= min(out_best, comp_best) + 20:
                        ok = True

                    if not ok:
                        print("> Skipped. Not shorter in outputs or compressed.")
                        continue

                    if test(problems[task_name], plain_code):
                        print(f"> Passed. plain size: {plain_len}, comp size: {comp_len}")
                        SUBS = SUBMISSION / task_name
                        SUBS.mkdir(exist_ok=True)
                        (SUBS / f"{plain_len:03d}_{args.comment}.py").write_bytes(plain_code.encode("L1"))
