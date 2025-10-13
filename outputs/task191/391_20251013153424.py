R=range(23)
e=enumerate
def p(g):
 P=[[x for*w,x in zip(*g,v)if 1in w]for v in g if 1in v]
 for t in range(8):
  P=(P[::-1],[*zip(*P)])[t%2]
  for y in range(-1,25-len(P)):
   for x in range(-1,25-len(P[0])):
    if~-any(23>i+y>=0<=j+x<23and g[i+y][j+x]&~1!=z&~1for i,v in e(P)for j,z in e(v)):
     for i,v in e(P):
      for j,z in e(v):
       if 23>i+y>=0<=j+x<23:g[i+y][j+x]=z
 return g