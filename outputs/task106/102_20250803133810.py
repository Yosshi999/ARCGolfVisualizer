def p(g):
    h=[v+w for v,w in zip(g,map(list,zip(*g[::-1])))]
    return h+[v[::-1]for v in h[::-1]]