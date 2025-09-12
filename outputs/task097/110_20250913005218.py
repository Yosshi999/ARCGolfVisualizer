e=enumerate
p=lambda g:[[w*(sum(sum(u[j-(j>0):j+2])for u in g[i-(i>0):i+2])>w)for j,w in e(v)]for i,v in e(g)]