def p(g):
    return[v[::-1] for v in [[w for w in v if w]for v in g] if v]