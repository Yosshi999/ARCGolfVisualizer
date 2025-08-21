e=enumerate
p=lambda g:[[g[i][j]*(sum(a>0for a in v[max(j-1,0):j+2]+[*w[max(i-1,0):i+2]])>3)for j,w in e(zip(*g))]for i,v in e(g)]