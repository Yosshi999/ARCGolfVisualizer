e=enumerate
def p(g):h=[*zip(*g)];I=h.index(max(h));return[(g[i-1],([4,0]*9)[I%2:][:len(v)])[sum(max(g[i:]))>0]for i,v in e(g)]