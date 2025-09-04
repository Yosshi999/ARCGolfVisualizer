r=range
def p(g):
 I,J=zip(*[(i,j)for i in r(10)for j in r(10)if g[i][j]]);m=min(I);n=min(J);exec("""
for i in r(m,m+5):
 for j in r(n,n+5):g[i][j]|=g[2*m+4-i][j]|g[j-n+m][i-m+n]"""*2);return g