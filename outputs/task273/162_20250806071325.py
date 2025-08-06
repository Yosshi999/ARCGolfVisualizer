def p(g):
 i=0
 while i<10:
  v=g[i];i+=1
  if 4in v:
   k=g.index(v,i);l=v.index(4)+1;r=9-v[::-1].index(4)
   for w in g[i:k]:w[l:r]=[2]*(r-l)
   i=k+1
 return g