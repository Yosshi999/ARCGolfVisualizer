def f(g):
 v=max(g,key=sum)
 l=len(v)
 m=l-v.count(0)
 for j in range(l):v[j]=max(v[j%m::m])
 return[*map(list,zip(*g))]
p=lambda g:f(f(g))