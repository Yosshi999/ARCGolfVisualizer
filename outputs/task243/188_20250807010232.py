e=enumerate
def p(g):
 for _ in[0]*900:
  for i,v in e(g):
   for j,w in e(v):
     if w<1 and ((i and g[i-1][j]==1)|(i<len(g)-1 and g[i+1][j]==1)|(1in v[max(j-1,0):j+2])):v[j]=1
 return g