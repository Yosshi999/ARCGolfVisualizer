r=range(9)
def p(g):
 for i in r:
  for j in r:
   if not(h:={*g[i][j:j+2],*g[i+1][j:j+2]})&{0,3}:
    for k in range(len(h)):g[i+k+2][j:j+2]=[3]*2
 return g