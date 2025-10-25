e=enumerate
def p(g):
 P=[[x for*w,x in zip(*g,v)if 1in w]for v in g if 1in v]
 for t in[0,1]*4:
  P=(P[::-1],[*zip(*P)])[t]
  for y in range(-1,25-len(P)):
   for x in range(-1,25-len(P[0])):
    if~-any(23>i+y>-1<j+x<23!=g[i+y][j+x]&4!=z&4for i,v in e(P)for j,z in e(v)):
     for i,v in e(P):
      for j,z in e(v):
       if 23>i+y>-1<j+x<23:g[i+y][j+x]=z
 return g