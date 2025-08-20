r=range(10)
def p(g):
 for c in[8,7,2,6]:g=[[(g[j][~i],c)[(j>0)*g[j-1][~i]==1]for j in r]for i in r]
 return g