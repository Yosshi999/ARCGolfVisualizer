e=enumerate
p=lambda g:[[2*(sum(sum(u[j-1:j+2])for u in g[i-1:i+2])==45)or w for j,w in e(v)]for i,v in e(g)]