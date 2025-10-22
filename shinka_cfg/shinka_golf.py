# %%

from shinka.core import EvolutionRunner, EvolutionConfig
from shinka.launch import LocalJobConfig
from shinka.database import DatabaseConfig

# ★ 必要: Gemini の API キー
import os
os.environ.setdefault("OPENAI_API_KEY", "*********************")

TASK = "task044"
SEED = f"../outputs/{TASK}/417_20250928183540.py"

evo = EvolutionConfig(
    task_sys_msg=(
        """あなたはPythonコードの「zlib圧縮後サイズ」を最小化する最適化エンジニアです。
        要件：
        - 全テスト合格を厳守（動作同一）。
        - 圧縮後サイズが小さくなるよう、トークンの再利用と反復を増やす。
        - 変数名や文字列リテラルは短縮し、同じ語を繰り返す。
        - 余計な説明は不要。変更後の完全なコードのみを出力。"""
    ),
    language="python",
    init_program_path=SEED,
    num_generations=60,
    max_parallel_jobs=6,
    patch_types=["diff","full"],
    patch_type_probs=[0.75,0.25],
    llm_models=["gpt-5-nano"],
    llm_kwargs={},
    max_patch_attempts=6,
    max_patch_resamples=3,
)

job = LocalJobConfig(
    eval_program_path="../judge/eval_golf.py",
    extra_cmd_args={"task": TASK, "outputs_root": "outputs"}
)

db = DatabaseConfig(
    num_islands=4,
    archive_size=100,
    elite_selection_ratio=0.3,
    migration_interval=8,
    migration_rate=0.15,
    parent_selection_strategy="power_law",
    exploitation_alpha=1.0,
    exploitation_ratio=0.2,
)

# %%

runner = EvolutionRunner(evo_config=evo, job_config=job, db_config=db)
runner.run()

# %%
