def f(g):
 for v in g:
  Q=[u for u in v if u>0]
  if (m:=len(Q))>1:
   c=v.index(Q[0]);Q=Q[m-c%m:]+Q[:m-c%m]
   for j in range(len(v)):v[j]=Q[j%m]
 return [*map(list,zip(*g))]
p=lambda g:f(f(g))