e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v):
   if j+1<len(v)and w*v[j+1]*g[i+1][j]:g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[4]*3;v[j-1]=v[j+1]=4;return g