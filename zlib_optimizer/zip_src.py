import ast
import keyword
import re
import random
import string
import math
import tokenize
import io
import zopfli.zlib as zlib

from .ast_unparse import unparse
import judge.core

def zip_src(src):
 if type(src) is bytes:
  src = src.decode("utf-8")
 newsrc = unparse(ast.parse(src))
 if len(newsrc) < len(src):
  src = newsrc
 # We prefer that compressed source not end in a quotation mark
 compressed = zlib.compress(src)[2:-4]

 def sanitize_for_quote_type(b_in, quote_type):
  """Clean up problematic bytes in compressed b-string for specific quote type"""
  b_out = bytearray()
  for i, b in enumerate(b_in):
   if b==0:
    # If the next character is [0-9], use \\x00 instead of \\0
    if i+1<len(b_in) and chr(b_in[i+1]).isdigit(): b_out += b"\\x00"
    else: b_out += b"\\0"
   elif b==ord("\r") and (quote_type == "'" or quote_type == '"'): b_out += b"\\r"
   elif b==ord("\\"): b_out += b"\\\\"
   elif b==ord("\n") and (quote_type == "'" or quote_type == '"'): b_out += b"\\n"
   elif quote_type == "'" and b==ord("'"): b_out += b"\\'"
   elif quote_type == '"' and b==ord('"'): b_out += b'\\"'
   else: b_out.append(b)
  return b"" + b_out

 # Try all quote types and find the shortest result
 if type(src) is str:
  src = src.encode()
 
 assert type(src) is bytes
 options = [src]

 # Option 1: Single quotes with escaping
 sanitized_single = sanitize_for_quote_type(compressed, "'")
 if max(sanitized_single) < 128:
  result_single = b"import zlib\nexec(zlib.decompress(b'" + sanitized_single + b"',-8))"
 else:
  result_single = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes('" + sanitized_single + b"','L1'),-8))"
 options.append(result_single)

 # Option 2: Double quotes with escaping
 sanitized_double = sanitize_for_quote_type(compressed, '"')
 if max(sanitized_double) < 128:
  result_double = b"import zlib\nexec(zlib.decompress(b\"" + sanitized_double + b'",-8))'
 else:
  result_double = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(\"" + sanitized_double + b'","L1"),-8))'
 options.append(result_double)

 # Option 3: Triple single quotes
 base_sanitized = bytearray()
 for i,b in enumerate(compressed):
  if   b==0:
   if i+1<len(compressed) and chr(compressed[i+1]).isdigit(): base_sanitized += b"\\x00"
   else: base_sanitized += b"\\0"
  elif b==ord("\r"): base_sanitized += b"\\r"
  elif b==ord("\\"): base_sanitized += b"\\\\"
  else: base_sanitized.append(b)
 base_sanitized = b"" + base_sanitized

 sanitized_triple_single = sanitize_for_quote_type(base_sanitized, "'''")
 if max(sanitized_triple_single) < 128:
  result_triple_single = b"import zlib\nexec(zlib.decompress(b'''" + sanitized_triple_single + b"''',-8))"
 else:
  result_triple_single = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes('''" + sanitized_triple_single + b"''','L1'),-8))"
 options.append(result_triple_single)

 # Option 4: Triple double quotes (original logic)
 sanitized_triple_double = sanitize_for_quote_type(base_sanitized, '"""')
 if max(sanitized_triple_double) < 128:
  result_triple_double = b"import zlib\nexec(zlib.decompress(b\"\"\"" + sanitized_triple_double + b'"""",-8))'
 else:
  result_triple_double = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(\"\"\"" + sanitized_triple_double + b'"""","L1"),-8))'
 options.append(result_triple_double)

 # Return the shortest option
 return min(options, key=len)

def create_template_from_function(code_string: str) -> (str, list):
 tree = ast.parse(code_string)
 variable_names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and node.id not in keyword.kwlist and node.id not in ['chain','enumerate', 'combinations', 'product', 'str', 'abs', 'exec','len', 'min', 'max', 'range', 'set','any', 'filter', 'list', 'map', 'sum', 'tuple', 'zip', 'all', 'sorted']}
 template = code_string
 for name in sorted(list(variable_names), key=len, reverse=True):
  template = re.sub(r'\b' + re.escape(name) + r'\b', f'##{name}##', template)
 return template.replace("def ##p##", "def p").replace("##p##=lambda", "p=lambda").replace("##f##'", "f'").replace('##f##"', 'f"'), sorted(list(variable_names))

import threading
from queue import Queue
import traceback

def validation_worker(queue, src, sample_case, terminate_flag):
  """
  テストケースを分割して実行し、全体の結果をキューに格納する。停止命令があれば中断する。
  """
  try:
   results = []
   for case in sample_case:
     if terminate_flag.is_set():
      queue.put(False)
      return
     result = judge.core.judge_code('taskXXX', src, [case])
     results.append(result.get("success", False) is True)
   queue.put(all(results))
  except Exception:
   queue.put(False)

def validate_code(src: str, sample_case: list, timeout_sec: float = 2.0) -> bool:
 """
 サブプロセスで validate_code を呼び出し、
 タイムアウト・例外・Kill された場合は False を返す。
 """

 queue = Queue()
 terminate_flag = threading.Event()
 p = threading.Thread(target=validation_worker, args=(queue, src, sample_case, terminate_flag))
 p.start()
 p.join(timeout_sec)

 if p.is_alive():
  terminate_flag.set()  # タイムアウトで強制終了
  return False

 return queue.get_nowait()

def run_optimizer(task_num: int, raw_function_string: str, sample_case: list, pruning_threshold: int = 500) -> str:
 """
 与えられたPython関数コード（def p(...) ...）を圧縮最適化し、
 焼きなまし探索 + 軽量 validate_code で最適化後のコード文字列を返す。
 """
 RAW_FUNCTION_STRING = raw_function_string.strip()

 # --- テンプレート作成（変数を ##var## に置換） ---
 FUNCTION_TEMPLATE, original_vars = create_template_from_function(RAW_FUNCTION_STRING)
 initial_code = FUNCTION_TEMPLATE.replace("##", "")
 base_size = len(zip_src(initial_code))

 # pruning_threshold 以上に大きければオリジナルを返す
 if base_size * 0.9 > pruning_threshold or base_size < 100:
  return zip_src(initial_code)

 # 変数名候補
 candidate_names = list(string.ascii_letters + '_')

 # 焼きなましパラメータ
 LIMIT = 10000
 T_init = 3.0
 T_final = 0.2
 cooling = math.exp(math.log(T_final / T_init) / LIMIT)

 current_mapping = {var: var for var in original_vars}
 current_code = initial_code
 current_size = base_size
 best_code, best_size = current_code, current_size
 T = T_init

 assert validate_code(current_code, sample_case) is True

 for i in range(LIMIT):
  if i % 500 == 0:
   print(f"[SA task{task_num:03d}] Iter {i}, T={T:.3f}, best={best_size}, current={current_size}")

  if not original_vars:
   continue

  # ランダムに一部の変数を置換
  trial_mapping = dict(current_mapping)
  num_changes = random.randint(1, min(3, len(trial_mapping)))
  vars_to_change = random.sample(original_vars, k=num_changes)
  for var, new_name in zip(vars_to_change, random.sample(candidate_names, k=num_changes)):
   trial_mapping[var] = new_name

  # テンプレートに適用
  trial_code = FUNCTION_TEMPLATE
  for var in original_vars:
   trial_code = trial_code.replace(f"##{var}##", trial_mapping[var])

  # 軽量 validate_code
  if validate_code(trial_code, sample_case) is False:
   continue  # テスト失敗なら採用しない

  # サイズ計測
  trial_size = len(zip_src(trial_code))

  # 焼きなまし判定
  delta = trial_size - current_size
  if delta <= 0 or random.random() < math.exp(-delta / T):
   current_code, current_size = trial_code, trial_size
   current_mapping = dict(trial_mapping)
   if trial_size < best_size:
    best_code, best_size = trial_code, trial_size
    print(f"[SA task{task_num:03d}] New best at iter {i+1}: size={best_size}")

  # 温度更新
  T = max(T * cooling, T_final)

 return zip_src(best_code)