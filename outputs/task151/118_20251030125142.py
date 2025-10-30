f=lambda g:g.index(max(g))
def p(g):i,j=f(g),f(g[k:=0]);exec('g[i-1+k][j-1:j+2]=4,k%2*g[i][j]or 4,4;k+=1;'*3);return g