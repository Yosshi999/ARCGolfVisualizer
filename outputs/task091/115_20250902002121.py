e=enumerate
def p(g):(i,j),*_,(I,J)=[(i,j)for i,v in e(g)for j,w in e(v)if w&1];return[v[j:J+1]for v in g[i-1:I+2]]