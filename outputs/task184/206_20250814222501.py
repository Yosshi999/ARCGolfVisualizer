s=lambda g:[-1]+[i for i,v in enumerate(g)if sum(v)<1]+[None]
def p(g):
 v=s(g)
 h=s(zip(*g))
 return[[max(a:=sum([v[l+1:r]for v in g[u+1:d]],[]),key=a.count)for l,r in zip(h,h[1:])]for u,d in zip(v,v[1:])]