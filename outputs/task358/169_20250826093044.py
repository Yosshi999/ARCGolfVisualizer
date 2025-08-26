def f(g):
 v=max(g,key=sum)
 Q=[u for u in v if u>0]
 m=len(Q)
 c=v.index(Q[0]);Q=Q[m-c%m:]+Q[:m-c%m]
 v[:]=(Q*9)[:len(v)]
 return[*map(list,zip(*g))]
p=lambda g:f(f(g))