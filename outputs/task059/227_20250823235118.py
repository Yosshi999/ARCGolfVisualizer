r=[0,4,8]
def p(g):
 f=lambda i,j:sum(sum([v[j:j+3]for v in g[i:i+3]],[]))
 m=max(f(i,j)for i in r for j in r)
 c,*_={*sum(g,[])}-{0,5}
 for i in r:
  for j in r:
   d=f(i,j)
   for v in g[i:i+3]:v[j:j+3]=[c*(d==m)]*3
 return g