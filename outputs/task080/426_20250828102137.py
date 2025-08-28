def p(g):
 n=len(g)
 d=2
 while g[0][d-2]==g[0][d-1]:d+=1
 for a in range(d):
  for b in range(d):
   for s in range(a+d,n-d,d):
    for t in range(b+d,n-d,d):
     if g[s-d][t]==g[s][t-d]==g[s][t+d]==g[s+d][t]>0:
      for i in range(a,n,d):
       for j in range(b,n,d):
        if g[i][j]==g[s][t]:
         for x in[-d,0,d]:
          for y in[-d,0,d]:
           if 0<=i+x<n and 0<=j+y<n:g[i+x][j+y]=g[s+x][t+y]
 return g