r=[0,3,6]
def p(g):
 for i in r:
  for j in r:
   for k in[0,1,2]*(g[i+1][j+5]>0):g[i+k][j+4:j+7]=g[k][:3]
 return g