r=range(17)
def p(g):v,h=zip(*[(i,j)for i in r for j in r if g[i][j]>7]);return[[(c:=g[i][j],3)[c&1*(min(v)<=i<=max(v))*(min(h)<=j<=max(h))]for j in r]for i in r]