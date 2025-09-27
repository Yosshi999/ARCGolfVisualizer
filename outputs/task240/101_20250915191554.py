r=range(19)
def p(g):
 for _ in r:g=[[g[j][i]|g[j][~i+2*(j+2<i<16-j)]for j in r]for i in r]
 return g