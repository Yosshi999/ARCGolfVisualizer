e=enumerate
t=lambda g:[v for v in zip(*g) if any(v)]
def p(g):
 M=[*map(list,g)]
 u,d=(y for y,v in e(g)if 4 in v)
 l,r=(x for x,c in e(g[u])if 4==c)
 for y,v in e(g):
  if u<=y<=d:v[l]=v[r]=0
 g=t(g)
 if max(g[0])-M[u+1][l]:g=g[::-1]
 g=t(g)
 for Y,v in e(g):
  M[u+Y+1][l+1:r]=v
 return[v[l:r+1]for v in M[u:d+1]]