e=enumerate
t=lambda g:[*filter(any,zip(*g))]
def p(g):
 M=eval(str(g))
 (u,l),*_,(d,r)=[(i,j)for i,v in e(g)for j,w in e(v)if w==4]
 for y,v in e(g):
  if u<=y<=d:v[l]=v[r]=0
 g=t(g)
 if max(g[0])-M[u+1][l]:g=g[::-1]
 g=t(g)
 for Y,v in e(g):M[u+Y+1][l+1:r]=v
 return[v[l:r+1]for v in M[u:d+1]]