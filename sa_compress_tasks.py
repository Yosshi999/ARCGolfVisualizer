import os
import glob
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

from zlib_optimizer.zip_src import run_optimizer
from judge.utils import load_problems_from_dir, get_local_shortest_submission
from zlib_optimizer.optimizer import optimize_code

BASE_DIR = Path(__file__).resolve().parent
PROBLEM_DIR = BASE_DIR / 'problems'
SUBMISSION = BASE_DIR / 'outputs'
ZLIB_SUBMISSION = BASE_DIR / 'compressed'


def process_single_task(task_num: int, problems):
    """1つのタスクフォルダを処理して結果を返す"""
    task_folder = f"outputs/task{task_num:03d}"
    compressed_folder = f"compressed/task{task_num:03d}"

    if not os.path.exists(task_folder):
        return None, f"スキップ: {task_folder} (フォルダが存在しません)"

    py_files = glob.glob(os.path.join(task_folder, "*.py"))
    if not py_files:
        return None, f"スキップ: {task_folder} (Pythonファイルが見つかりません)"

    logs = [f"処理中: {task_folder} ({len(py_files)} ファイル)"]

    # 元ファイルを読み込む
    file_contents = {}
    for py_file in py_files:
        try:
            with open(py_file, "rb") as f:
                content = f.read()
                file_contents[py_file] = content
        except Exception as e:
            print(f"  エラー読み取り {py_file}: {e}")
            continue

    min_size = get_local_shortest_submission(f"task{task_num:03d}", SUBMISSION, ZLIB_SUBMISSION).best_bytes

    # 圧縮
    compressed_results = []
    for py_file, content in file_contents.items():
        try:
            sample_case = problems[f"task{task_num:03d}"][-2:]
            try:
                code = optimize_code(content.decode("L1"))
            except Exception as e:
                code = content.decode("L1")
            print(f"  圧縮中: {py_file} (start: {len(content)} bytes -> {len(code)} bytes)")
            compressed = run_optimizer(task_num, code, sample_case,
                                       pruning_threshold=min_size)
            compressed_size = len(compressed)
            compressed_results.append((py_file, compressed, compressed_size))
            min_size = min(min_size, compressed_size)
            print(f"  {py_file}: {len(content)} → {compressed_size} bytes")
        except Exception as e:
            print(f"  圧縮エラー {py_file}: {e}")
            continue

    if not compressed_results:
        return None, "\n".join(logs)

    # 最短を選ぶ
    best_file, best_compressed_content, best_compressed_size = min(compressed_results, key=lambda x: x[2])

    if best_compressed_size < min_original_size:
        compressed_filename = os.path.join(compressed_folder, f"{best_compressed_size}_compressed.py")
        try:
            with open(compressed_filename, "wb") as f:
                f.write(best_compressed_content)

            improvement = min_original_size - best_compressed_size
            improvement_pct = (improvement / min_original_size) * 100
            print(f"  ✓ 保存: {compressed_filename}")
            print(f"  改善: {improvement} bytes ({improvement_pct:.1f}%短縮)")

            return {
                "task": task_folder,
                "original_file": os.path.basename(best_file),
                "original_size": len(file_contents[best_file]),
                "min_original_size": min_original_size,
                "compressed_size": best_compressed_size,
                "improvement": improvement,
                "improvement_pct": improvement_pct,
            }, "\n".join(logs)
        except Exception as e:
            print(f"  保存エラー {compressed_filename}: {e}")
    else:
        print(f"  スキップ: 圧縮版 ({best_compressed_size}) が元の最短 ({min_original_size}) より長い")

    return None, "\n".join(logs)


def process_tasks():
    problems = load_problems_from_dir(PROBLEM_DIR)
    results = []

    num_workers = multiprocessing.cpu_count()
    print(f"CPU数: {num_workers} → 並列実行します")

    task_nums = range(1, 401)  # 処理したいタスク番号のリスト

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(process_single_task, task_num, problems): task_num for task_num in task_nums}
        for future in as_completed(futures):
            result, log = future.result()
            if log:
                print(log)
            if result:
                results.append(result)

    # 集計
    if results:
        print(f"\n=== 圧縮結果要約 ===")
        print(f"圧縮が有効だったタスク: {len(results)}")
        total_original = sum(r["min_original_size"] for r in results)
        total_compressed = sum(r["compressed_size"] for r in results)
        total_improvement = total_original - total_compressed
        total_improvement_pct = (total_improvement / total_original) * 100 if total_original > 0 else 0

        print(f"合計節約: {total_improvement} bytes ({total_improvement_pct:.1f}%)")

        top_improvements = sorted(results, key=lambda x: x["improvement"], reverse=True)[:5]
        print(f"\n最も改善されたタスク (Top 5):")
        for r in top_improvements:
            print(f"  {r['task']}: {r['improvement']} bytes ({r['improvement_pct']:.1f}%)")
    else:
        print("\n圧縮が有効だったタスクはありませんでした。")


if __name__ == "__main__":
    process_tasks()
