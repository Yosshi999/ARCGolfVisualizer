from argparse import ArgumentParser
import zipfile
import json
from pathlib import Path
import importlib.util
import copy


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

REPO = Path(__file__).absolute().parent.parent
PROBLEM = REPO / 'problems'
SUBMISSION = REPO / 'outputs'
problems = {}
for p in sorted(PROBLEM.glob('*.json')):
    with open(p, 'r') as f:
        data = json.load(f)
        problems[p.stem] = data["train"] + data["test"] + data["arc-gen"]
print(f"found tasks: {len(problems)}")

with zipfile.ZipFile(args.zip, 'r') as zip_ref:
    for name in zip_ref.namelist():
        if name.endswith('.py'):
            with zip_ref.open(name) as f:
                task_name = name.split(".")[0]
                code = f.read().decode('utf-8')
                print(f"Processing {task_name}...")
                assert task_name in problems, f"Task {task_name} not found in problems."
                if test(problems[task_name], code):
                    print(f"> Passed. size: {len(code)}")
                    SUBS = SUBMISSION / task_name
                    SUBS.mkdir(exist_ok=True)
                    (SUBS / f"{len(code):03d}_{args.comment}.py").write_bytes(code.encode("utf-8"))

