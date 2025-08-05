def p(g):
 for _ in[0]*4:
  if g[0][2]==g[2][0]==8:
   g=[[g[i//3][j//3]*(g[i+3][j+3]>0)for j in range(6)]for i in range(6)]
  g=[*map(list,zip(*g[::-1]))]
 return g