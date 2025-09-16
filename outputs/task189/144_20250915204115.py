r=range(6)
def p(g):
 for _ in[0]*4:
  if g[0][2]==g[2][0]==8:g=[[g[i>2][j>2]*g[i+3][j+3]/3for j in r]for i in r]
  g=[*zip(*g[::-1])]
 return g