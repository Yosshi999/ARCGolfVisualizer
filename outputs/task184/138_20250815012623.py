s=lambda g:zip(v:=[0,*(i for i,v in enumerate(g)if~-any(v)),99],v[1:])
p=lambda g:[[max(g[u+1][l:r])for l,r in s(zip(*g))]for u,_ in s(g)]