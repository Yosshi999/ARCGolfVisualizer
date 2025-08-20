f=lambda g:[*map(all,g)].index(1);
def p(g):i,j=f(g),f(zip(*g));g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[4]*3;g[i][j-1]=g[i][j+1]=4;return g