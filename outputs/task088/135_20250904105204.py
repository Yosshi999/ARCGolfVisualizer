e=enumerate
def p(g):(i,j),*_,(k,l)=[(i,j)for i,v in e(g)for j,w in e(v)if w];return[[g[i][j]*(w>0)for w in v[j+1:l]]for v in g[i+1:k]]