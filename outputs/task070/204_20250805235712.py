r=range(17)
def p(g):
 v=[i for i in r for j in r if g[i][j]==8]
 h=[j for i in r for j in r if g[i][j]==8]
 return[[(g[i][j],3)[g[i][j]==1and min(v)<=i<=max(v)and min(h)<=j<=max(h)]for j in r]for i in r]