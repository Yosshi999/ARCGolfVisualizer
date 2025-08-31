import os
import glob

from judge.src_zip import zip_src

def process_tasks():
    """各タスクフォルダのPythonファイルを処理し、圧縮版が有効なら保存"""
    
    results = []
    
    for task_num in range(1, 401):  # task001 to task400
        task_folder = f"outputs/task{task_num:03d}"
        
        if not os.path.exists(task_folder):
            print(f"スキップ: {task_folder} (フォルダが存在しません)")
            continue
            
        # フォルダ内のすべての.pyファイルを取得
        py_files = glob.glob(os.path.join(task_folder, "*.py"))
        
        if not py_files:
            print(f"スキップ: {task_folder} (Pythonファイルが見つかりません)")
            continue
            
        print(f"処理中: {task_folder} ({len(py_files)} ファイル)")
        
        # 元ファイルの最短長を取得
        original_sizes = []
        file_contents = {}
        
        for py_file in py_files:
            try:
                with open(py_file, 'rb') as f:
                    content = f.read()
                    file_contents[py_file] = content
                    original_sizes.append(len(content))
            except Exception as e:
                print(f"  エラー読み取り {py_file}: {e}")
                continue
        
        if not original_sizes:
            continue
            
        min_original_size = min(original_sizes)
        
        # 各ファイルを圧縮し、最短の圧縮版を見つける
        compressed_results = []
        
        for py_file, content in file_contents.items():
            try:
                compressed = zip_src(content)
                compressed_size = len(compressed)
                compressed_results.append((py_file, compressed, compressed_size))
                print(f"  {os.path.basename(py_file)}: {len(content)} → {compressed_size} bytes")
            except Exception as e:
                print(f"  圧縮エラー {py_file}: {e}")
                continue
        
        if not compressed_results:
            continue
            
        # 最短の圧縮版を見つける
        best_compressed = min(compressed_results, key=lambda x: x[2])
        best_file, best_compressed_content, best_compressed_size = best_compressed
        
        # 圧縮版が元の最短より短い場合のみ保存
        if best_compressed_size < min_original_size:
            # 圧縮ファイルを保存
            compressed_filename = os.path.join(task_folder, f"{best_compressed_size}_compressed.py")
            try:
                with open(compressed_filename, 'wb') as f:
                    f.write(best_compressed_content)
                
                improvement = min_original_size - best_compressed_size
                improvement_pct = (improvement / min_original_size) * 100
                
                print(f"  ✓ 保存: {compressed_filename}")
                print(f"  改善: {improvement} bytes ({improvement_pct:.1f}%短縮)")
                
                results.append({
                    'task': task_folder,
                    'original_file': os.path.basename(best_file),
                    'original_size': len(file_contents[best_file]),
                    'min_original_size': min_original_size,
                    'compressed_size': best_compressed_size,
                    'improvement': improvement,
                    'improvement_pct': improvement_pct
                })
                
            except Exception as e:
                print(f"  保存エラー {compressed_filename}: {e}")
        else:
            print(f"  スキップ: 圧縮版 ({best_compressed_size}) が元の最短 ({min_original_size}) より長い")
    
    # 結果の要約を表示
    if results:
        print(f"\n=== 圧縮結果要約 ===")
        print(f"圧縮が有効だったタスク: {len(results)}")
        total_original = sum(r['min_original_size'] for r in results)
        total_compressed = sum(r['compressed_size'] for r in results)
        total_improvement = total_original - total_compressed
        total_improvement_pct = (total_improvement / total_original) * 100 if total_original > 0 else 0
        
        print(f"合計節約: {total_improvement} bytes ({total_improvement_pct:.1f}%)")
        
        # 最も改善されたタスクトップ5
        top_improvements = sorted(results, key=lambda x: x['improvement'], reverse=True)[:5]
        print(f"\n最も改善されたタスク (Top 5):")
        for r in top_improvements:
            print(f"  {r['task']}: {r['improvement']} bytes ({r['improvement_pct']:.1f}%)")
    else:
        print("\n圧縮が有効だったタスクはありませんでした。")

if __name__ == "__main__":
    process_tasks()