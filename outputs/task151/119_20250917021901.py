f=lambda g:g.index(max(g))
def p(g):i,j=f(g),f(g[0]);g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[4]*3;g[i][j-1:j+2:2]=4,4;return g