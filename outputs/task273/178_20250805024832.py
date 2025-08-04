def p(g):
 i=0
 while i<10:
  v=g[i];i+=1
  if 4in v:
   k=g.index(v,i)
   for j in range(i,k):
    l=v.index(4)+1;r=9-v[::-1].index(4)
    g[j][l:r]=[2]*(r-l)
   i=k+1
 return g