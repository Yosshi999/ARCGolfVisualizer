e=enumerate
def p(g):I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w&1]);return[v[min(J):max(J)+1]for v in g[min(I)-1:max(I)+2]]