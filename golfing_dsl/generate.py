from astsurgeon import minify
from hashlist import hashes
from pathlib import Path
import importlib.util
import copy
import json

def generate(task_number: int) -> str:
    unified = (Path(__file__).parent / "common_header.py").read_text()
    unified += "\n" + (Path(__file__).parent / "arc-dsl/solvers.py").read_text()
    unified = unified.replace("__solve__", f"solve_{hashes[task_number]}")
    minified_code = minify(unified)
    return minified_code

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 2:
#         print("Usage: python generate.py <task_number>")
#         sys.exit(1)
#     task_number = int(sys.argv[1])
#     minified_code = generate(task_number)
#     print(minified_code)

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

if __name__ == "__main__":
    REPO = Path(__file__).absolute().parent.parent
    PROBLEM = REPO / 'problems'
    SUBMISSION = REPO / 'outputs'
    problems = {}
    for p in sorted(PROBLEM.glob('*.json')):
        with open(p, 'r') as f:
            data = json.load(f)
            problems[p.stem] = data["train"] + data["test"] + data["arc-gen"]
    print(f"found tasks: {len(problems)}")

    for i in range(105,400):
        task_name = f"task{i+1:03d}"
        code = generate(i)
        print("Testing task:", task_name)
        if test(problems[task_name], code):
            print(f"> Passed. size: {len(code)}")
            SUBS = SUBMISSION / task_name
            SUBS.mkdir(exist_ok=True)
            (SUBS / f"{len(code):03d}_fromdsl.py").write_bytes(code.encode("utf-8"))

