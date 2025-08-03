import common

def p(g):
    """入力グリッド g から出力グリッドに変換する関数"""
    height, width = len(g), len(g[0])
    
    # 入力グリッドから青いピクセルの位置を取得
    blue_pixels = []
    for r in range(height):
        for c in range(width):
            if g[r][c] == common.blue():
                blue_pixels.append((r, c))
    
    if not blue_pixels:
        # ピクセルがない場合は空の出力グリッドを返す
        return common.grid(width, 9)
    
    # ステップサイズの推定
    # 青いピクセルの行をグループ化
    row_groups = {}
    for r, c in blue_pixels:
        if r not in row_groups:
            row_groups[r] = []
        row_groups[r].append(c)
    
    # パターンの繰り返し間隔を検出
    steps = 2  # デフォルト値
    rows = sorted(row_groups.keys())
    
    # より正確なステップサイズの推定
    if len(rows) >= 4:
        # 行0と行2のパターンが同じかチェック（steps=2の場合）
        if len(rows) >= 3 and 0 in row_groups and 2 in row_groups:
            if sorted(row_groups[0]) == sorted(row_groups[2]):
                steps = 2
        # 行0と行3のパターンが同じかチェック（steps=3の場合）
        elif len(rows) >= 4 and 0 in row_groups and 3 in row_groups:
            if sorted(row_groups[0]) == sorted(row_groups[3]):
                steps = 3
    
    # 基本パターンの抽出（最初のsteps行分）
    base_pattern = [(r, c) for r, c in blue_pixels if r < steps]
    
    # フリップの検出
    flip = 0
    if height >= 2 * steps and base_pattern:
        # 最初のパターンと次のパターンを比較してフリップを検出
        first_row_cols = [c for r, c in base_pattern if r == 0]
        second_offset_cols = [c for r, c in blue_pixels if r == steps]
        
        if first_row_cols and second_offset_cols:
            # 左右反転した場合の期待値
            expected_flipped_cols = [width - c - 1 for c in first_row_cols]
            if set(second_offset_cols) == set(expected_flipped_cols):
                flip = 1
    
    # 出力グリッドの生成（拡張された高さ）
    extended = 9  # デフォルトの拡張高さ
    output = common.grid(width, extended)
    
    # パターンを出力グリッドに拡張して配置
    flipped = 0
    for offset in range(0, extended, steps):
        for r, c in base_pattern:
            new_r = offset + r
            if new_r < extended:
                # フリップの状態に応じて列を調整
                new_c = c if flipped == 0 else width - c - 1
                output[new_r][new_c] = common.red()
        
        # フリップ状態を切り替え
        if flip == 1:
            flipped = 1 - flipped
    
    return outputaaaa