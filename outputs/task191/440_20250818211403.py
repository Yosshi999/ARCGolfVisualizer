R=range(23)
e=enumerate
def p(g):
 v,h=zip(*((i,j)for i in R for j in R if g[i][j]==1));u,*_,d=v;l,*_,r=h;P=[v[l:r+1]for v in g[u:d+1]]
 for t in range(8):
  g=(g[::-1],[*map(list,zip(*g))])[t%2]
  for y in range(-1,24-d+u):
   for x in range(-1,24-r+l):
    if all(not(23>i+y>=0<=j+x<23)or g[i+y][j+x]&~1==z&~1for i,v in e(P)for j,z in e(v)):
     for i,v in e(P):
      for j,z in e(v):
       if 23>i+y>=0<=j+x<23:g[i+y][j+x]=z
 return g