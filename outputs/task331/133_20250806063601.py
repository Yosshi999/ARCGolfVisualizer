r=range(10)
def p(g):
 for c in[8,6,2,7]:g=[*map(list,zip(*[[(g[i][j],c)[(i>0)*g[i-1][j]==1]for j in r]for i in r][::-1]))]
 return g