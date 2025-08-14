e=enumerate
def p(g):t=[(i,j)for i,v in e(g)for j,w in e(v)if w&1];i,j=min(t);I,J=max(t);return[v[j:J+1]for v in g[i-1:I+2]]