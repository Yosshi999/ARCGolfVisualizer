e=enumerate
def p(g):I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w]);i=sum(I)//2;j=sum(J)//2;g[i][j-1:j+2]=[3]*3;g[i-1][j]=g[i+1][j]=3;return g