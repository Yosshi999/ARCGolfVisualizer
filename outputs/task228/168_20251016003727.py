e=enumerate
p=lambda g:exec('(u,l),*_,(d,r)=[(i+1,j+1)for i,v in e(g)for j,w in e(v)if~-v.count(w)*w];g[u][l],g[d][r]=g[d][r],g[u][l];g[::-1]=map(list,zip(*g));'*4)or g