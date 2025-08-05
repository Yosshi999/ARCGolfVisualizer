def p(g):
    h, w = len(g), len(g[0])
    # Find rectangles and check for holes
    colors = set()
    for r in range(h):
        for c in range(w):
            if g[r][c] != 0:
                colors.add(g[r][c])
    
    for color in colors:
        # Check if this color forms a rectangle with a hole
        min_r, max_r, min_c, max_c = h, -1, w, -1
        # Find bounding box of this color
        for r in range(h):
            for c in range(w):
                if g[r][c] == color:
                    min_r, max_r = min(min_r, r), max(max_r, r)
                    min_c, max_c = min(min_c, c), max(max_c, c)
        
        # Check if there's a hole inside this rectangle
        has_hole = False
        for r in range(min_r + 1, max_r):
            for c in range(min_c + 1, max_c):
                if g[r][c] == 0:
                    has_hole = True
                    break
            if has_hole:
                break
        
        if has_hole:
            return [[color]]
    
    return [[0]]