e=enumerate
def p(g):
 (a,*_,A),(b,*_,B)=map(sorted,zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w==5]))
 C=sum({*sum(g,[])})-5
 for v in g[a+1:A]:v[b+1]=v[B-1]=C
 for j in range(b+1,B):g[a+1][j]=g[A-1][j]=C
 return g