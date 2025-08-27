e=enumerate
def f(g):
 I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w])
 m=min(I);M=max(I);n=min(J);N=max(J)
 return[*map(list,zip(*[v[:n]+[w or 2*(v[n+1:N].count(1)>1 or v in[g[m],g[M]])for w in v[n:N+1]]+v[N+1:]for v in g]))]
p=lambda g:f(f(g))