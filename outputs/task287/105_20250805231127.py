r=range(16)
def p(g):
 h=[[max({g[i][j],g[~i][j],g[i][~j],g[~i][~j]}-{4})for j in r]for i in r]
 return h