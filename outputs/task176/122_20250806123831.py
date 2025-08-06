def p(g):
 r=range(len(g[0]))
 for i in r:
  if 4<i%12<8:g[0][i]=4
  if i%6==0:g[1][i]=4
  if -~i%12<3:g[2][i]=4
 return g