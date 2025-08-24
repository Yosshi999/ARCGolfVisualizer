r=[0,3,6]
def p(g):
 for i in r:
  for j in r:
   for k in r*g[i+1][j+5]:g[i+k//3][j+4:j+7]=g[k//3][:3]
 return g