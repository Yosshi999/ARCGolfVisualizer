from argparse import ArgumentParser
import zipfile
import json
from pathlib import Path
import importlib.util
import copy
import zlib
import base64
import re


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

def get_local_shortest_submission(task: str):
    subs = SUBMISSION / task
    if not subs.exists():
        return None
    py_files = list(subs.glob("*.py"))
    if not py_files:
        return None
    return min(py_files, key=lambda x: int(x.stem.split('_')[0]))

def normalize_code(code: str) -> str:
    return code.strip().replace("\r\n", "\n")

def get_local_shortest_bytes(task: str):
    sub = get_local_shortest_submission(task)
    if sub is None:
        return float('inf')
    return int(sub.stem.split('_')[0])

def get_local_shortest_compressed_bytes(task: str):
    subs = COMPRESSED / task
    if not subs.exists():
        return float('inf')
    py_files = list(subs.glob("*.py"))
    if not py_files:
        return float('inf')
    return min(int(x.stem.split('_')[0]) for x in py_files)

def is_zlib_code(code: str) -> bool:
    return code.startswith("#coding:L1")

def decode_zlib(code: str) -> str:
    # zlib.decompress(...) の呼び出し部分を抜き出す
    m = re.search(r'(zlib\.decompress\s*\(.*\))', code, re.S)
    if not m:
        raise ValueError("Unable to find zlib.decompress(...) expression")
    expr = m.group(1)
    # zlib と bytes だけを許可して評価
    data = eval(expr, {"zlib": zlib, "bytes": bytes})
    return data.decode("utf-8")

with zipfile.ZipFile(args.zip, 'r') as zip_ref:
    for name in zip_ref.namelist():
        if name.endswith('.py'):
            with zip_ref.open(name) as f:
                task_name = name.split("/")[-1].split(".")[0]
                code = normalize_code(f.read().decode('utf-8'))
                print(f"Processing {task_name}...")

                if not task_name in problems:
                    print(f"> Skipped. Task {task_name} not found in problems.")
                    continue

                if not is_zlib_code(code):
                    # normal case
                    if get_local_shortest_bytes(task_name) < len(code):
                        print(f"> Skipped. Local shortest submission is shorter.")
                        continue
                    if test(problems[task_name], code):
                        print(f"> Passed. size: {len(code)}")
                        SUBS = SUBMISSION / task_name
                        SUBS.mkdir(exist_ok=True)
                        (SUBS / f"{len(code):03d}_{args.comment}.py").write_bytes(code.encode("utf-8"))
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
                    elif comp_len <= comp_best + 20:
                        ok = True

                    if not ok:
                        print("> Skipped. Not shorter in outputs or compressed.")
                        continue

                    if test(problems[task_name], plain_code):
                        print(f"> Passed. plain size: {plain_len}, comp size: {comp_len}")
                        SUBS = SUBMISSION / task_name
                        SUBS.mkdir(exist_ok=True)
                        (SUBS / f"{plain_len:03d}_{args.comment}.py").write_bytes(plain_code.encode("utf-8"))
                        COMP = COMPRESSED / task_name
                        COMP.mkdir(exist_ok=True)
                        (COMP / f"{comp_len:03d}_{args.comment}.py").write_bytes(code.encode("utf-8"))
