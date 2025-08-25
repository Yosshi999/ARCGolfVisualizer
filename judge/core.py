import json
import re
import io
import importlib.util
import traceback
import contextlib
import copy
from typing import Tuple, Dict, Any
import numpy

# Keep normalize_code here so that both app and CI can call it
def normalize_code(code: str) -> str:
    return code.strip().replace("\r\n", "\n")

# Main judging function: returns a structured dict similar to your Flask responses
def judge_code(task: str, code: str, examples: list) -> Dict[str, Any]:
    code = normalize_code(code)

    try:
        task_modname = "task_with_imports"
        spec = importlib.util.spec_from_loader(task_modname, loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(code, module.__dict__)

        if not hasattr(module, "p"):
            return {"success": False, "error_type": "function_missing", "error_message": "Unable to locate function p()."}
        program = getattr(module, "p")
        if not callable(program):
            return {"success": False, "error_type": "not_callable", "error_message": "p() is not callable."}

        mismatch = []
        for i, example in enumerate(examples):
            input_data = copy.deepcopy(example["input"])
            expected_output = copy.deepcopy(example["output"])

            with contextlib.redirect_stdout(io.StringIO()) as fp:
                output = program(input_data)
                stdoutLog = fp.getvalue()

            # JSON normalization
            try:
                result = json.dumps(output)
                # Kaggle json might include true/false; original code mapped those to 1/0
                result = result.replace("true", "1").replace("false", "0")
                # allow digits, arrays, spaces, commas, dots and minus sign
                unsafe_chars = re.compile(r"[^0-9,\[\]\s\.\-]")
                if unsafe_chars.search(result):
                    return {"success": False, "error_type": "type_error", "error_message": f"Invalid output format: {result[:500]}"}
                output = json.loads(result)
            except Exception as e:
                return {"success": False, "error_type": "type_error", "error_message": f"Output format error: {str(e)}"}

            # Use numpy array comparison
            try:
                user_output = numpy.array(output)
                label_output = numpy.array(expected_output)
                if not numpy.array_equal(user_output, label_output):
                    mismatch.append({"index": i, "output": output, "stdoutLog": stdoutLog})
            except Exception as e:
                return {"success": False, "error_type": "array_error", "error_message": f"Array comparison error: {str(e)}"}

        if len(mismatch) > 0:
            return {"success": False, "error_type": "test", "mismatch": mismatch}

        return {"success": True}

    except Exception as e:
        tb = traceback.format_exc()
        return {"success": False, "error_type": "execution", "error_message": str(e) + "\n" + tb}


# convenience wrapper to judge code read from a file-like object / path
from pathlib import Path

def judge_file(task: str, file_path: Path, examples: list) -> Dict[str, Any]:
    code = file_path.read_text(encoding="utf-8")
    return judge_code(task, code, examples)
