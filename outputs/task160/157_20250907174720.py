def p(g):
 for k in range(64):
  i=k//8;j=k%8
  if all(g[i+x][j:j+3]==[1,1-x%2,1]for x in[0,1,2]):
   for x in[0,1,2]:g[i+x][j:j+3]=[x%2*2,2,x%2*2]
 return g