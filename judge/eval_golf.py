# judge/eval_golf.py
import argparse, json, os, sys, time, fcntl, traceback
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # repo root を import path に
from judge.core import judge_code                     # ← ここだけ、あなたのAPIに合わせて
from judge.utils import load_problems_from_dir
from zlib_optimizer.zip_src import zip_src               # ← 圧縮関数（存在しない場合は差し替え）

PENALTY = -10_000_000.0
PROBLEM = Path(__file__).parent.parent / 'problems'

def compressed_len(code: str) -> int:
    # あなたの実装に合わせる: zopfli でも zlib でもOK。bytes を返す関数を想定
    data = zip_src(code)     # bytes を返す想定
    return len(data)          # 既存の算式に合わせて必要なら調整

def safe_int(x, default=10**9):
    try:
        return int(x)
    except:
        return default

def update_best_if_better(task_dir: Path, code: str, clen: int):
    """ベストを更新したら outputs/taskXXX/ に保存（原子的に .best_len.json を更新）"""
    best_file = task_dir / ".best_len.json"
    best = {"clen": 10**9, "file": ""}
    try:
        if best_file.exists():
            best = json.loads(best_file.read_text(encoding="utf-8"))
    except:
        pass

    if clen >= safe_int(best.get("clen", 10**9)):
        return False, best  # 改善なし

    # 原子的更新（ロック）
    with open(best_file, "a+", encoding="utf-8") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        fh.seek(0)
        try:
            cur = json.loads(fh.read() or "{}")
        except:
            cur = {}
        cur_clen = safe_int(cur.get("clen", 10**9))
        if clen < cur_clen:  # 二重実行でもOK
            ts = time.strftime("%Y%m%d%H%M%S")
            out_name = f"{clen}_{ts}_shinka.py"
            (task_dir / out_name).write_text(code, encoding="utf-8")
            cur = {"clen": clen, "file": out_name}
            fh.seek(0); fh.truncate(0); fh.write(json.dumps(cur))
        fcntl.flock(fh, fcntl.LOCK_UN)
    return True, cur

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--program_path")
    p.add_argument("--results_dir")
    p.add_argument("candidate_path", nargs="?")
    p.add_argument("--task", required=True)
    p.add_argument("--outputs_root", default="outputs")
    p.add_argument("--emit_json", action="store_true")
    args = p.parse_args()

    cand = Path(args.candidate_path or args.program_path)
    task_dir = Path(args.outputs_root) / args.task
    task_dir.mkdir(parents=True, exist_ok=True)

    try:
        code = cand.read_text(encoding="utf-8")
    except Exception:
        print(f'Error reading candidate file: {cand}')
        print(PENALTY); return

    try:
        clen = compressed_len(code)
    except Exception:
        print(f'Error compressing candidate code: {cand}')
        print(PENALTY); return
    
    try:
        problems = load_problems_from_dir(PROBLEM)
        testcases = problems[args.task][-20:-10]
    except Exception:
        traceback.print_exc(file=sys.stderr)
        print(PENALTY); return

    try:
        ok = judge_code('shinka', code, testcases)  # ← ここだけ、あなたのAPIに合わせて
        passed = ok['success']
        score = -float(clen) if passed else PENALTY
        if passed:
            improved, best = update_best_if_better(task_dir, code, clen)
        else:
            improved, best = (False, {})
    except Exception:
        # デバッグしたい場合は環境変数で traceback を吐く
        if os.environ.get("EVAL_DEBUG") == "1":
            traceback.print_exc(file=sys.stderr)
        print(PENALTY); return

    if args.emit_json:
        payload = {"score": score, "compressed_len": clen, "passed": passed}
        print(json.dumps(payload))
    else:
        print(score)

if __name__ == "__main__":
    main()
