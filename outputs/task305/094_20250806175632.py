r=range(16)
def p(g):c=len({*sum(g,[])})-1;return[[max(g[0][(i+j)%c::c])for j in r]for i in r]