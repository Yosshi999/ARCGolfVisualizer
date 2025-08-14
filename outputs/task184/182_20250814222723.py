s=lambda g:zip(v:=[-1]+[i for i,v in enumerate(g)if sum(v)<1]+[None],v[1:])
p=lambda g:[[max(a:=sum([v[l+1:r]for v in g[u+1:d]],[]),key=a.count)for l,r in s(zip(*g))]for u,d in s(g)]