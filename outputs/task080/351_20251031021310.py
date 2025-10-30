def p(g):
 e=len(g)
 n=2
 while g[n-2]==g[n-1]:n+=1
 for l in range(n,e-n):
  for d in range(n,e-n):
   if g[l-n][d]==g[l][d-n]==g[l][d+n]==g[l+n][d]>0:
    for u in range(l%n,e,n):
     for f in range(d%n,e,n):
      if g[u][f]==g[l][d]:
       for a in[-n,0,n]:
        for i in[-n,0,n]:
         if e>u+a>=0<=f+i<e:g[u+a][f+i]=g[l+a][d+i]
 return g