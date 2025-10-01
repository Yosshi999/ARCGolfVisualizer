from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass
import json
from .core import normalize_code

# Return Path to shortest .py file under submission_dir / task
def _get_shortest_submission(submission_dir: Path, task: str, encoding='utf-8') -> Optional[Path]:
    subs = submission_dir / task
    if not subs.exists():
        return None
    py_files = list(subs.glob("*.py"))
    if not py_files:
        return None
    return min(py_files, key=lambda fn: len(normalize_code(fn.read_text(encoding=encoding))))

@dataclass
class ShortestSubmission:
    """情報を一括で保持する構造体"""
    normal_path: Optional[Path]
    compressed_path: Optional[Path]
    best_path: Optional[Path]
    normal_bytes: Optional[int]
    compressed_bytes: Optional[int]
    best_bytes: Optional[int]

    def to_dict(self) -> Dict[str, Any]:
        """テンプレートやAPIでそのまま使えるようdict化"""
        return {
            "normal_path": str(self.normal_path) if self.normal_path else None,
            "compressed_path": str(self.compressed_path) if self.compressed_path else None,
            "best_path": str(self.best_path) if self.best_path else None,
            "normal_bytes": self.normal_bytes,
            "compressed_bytes": self.compressed_bytes,
            "best_bytes": self.best_bytes,
        }


def get_local_shortest_submission(task: str, submission_dir: Path, compressed_dir: Path) -> ShortestSubmission:
    """
    指定した task の提出について
    - 通常提出
    - 圧縮提出
    - 両者で短い方（best）
    の情報をまとめて返す
    """
    # 通常提出
    normal_path = _get_shortest_submission(submission_dir, task)
    normal_bytes = None
    if normal_path:
        normal_bytes = len(normalize_code(normal_path.read_text()))

    # 圧縮提出
    compressed_path = _get_shortest_submission(compressed_dir, task, encoding='L1')
    compressed_bytes = None
    if compressed_path:
        compressed_bytes = len(normalize_code(compressed_path.read_text(encoding='L1')))

    # best 判定
    best_path, best_bytes = None, None
    candidates = [
        (normal_path, normal_bytes),
        (compressed_path, compressed_bytes),
    ]
    candidates = [(p, b) for p, b in candidates if p and b is not None]
    if candidates:
        best_path, best_bytes = min(candidates, key=lambda x: x[1])

    return ShortestSubmission(
        normal_path=normal_path,
        compressed_path=compressed_path,
        best_path=best_path,
        normal_bytes=normal_bytes,
        compressed_bytes=compressed_bytes,
        best_bytes=best_bytes,
    )

# Helper to load problems from a directory (matches original behavior)
def load_problems_from_dir(problems_dir: Path):
    problems = {}
    for p in sorted(problems_dir.glob('*.json')):
        with p.open('r', encoding='utf-8') as f:
            data = json.load(f)
            problems[p.stem] = data.get("train", []) + data.get("test", []) + data.get("arc-gen", [])
    return problems
