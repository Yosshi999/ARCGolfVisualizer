def p(g):
 a=b=30;c=d=0;r=range(len(g));R=range(len(g[0]))
 for i in r:
  for j in R:
   if g[i][j]:a=min(a,i);b=min(b,j);c=max(c,i);d=max(d,j)
 return[[(e:=g[i][j],2)[e<(a<=i<=c)*(b<=j<=d)]for j in R]for i in r]