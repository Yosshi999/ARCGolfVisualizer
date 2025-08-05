def p(g):
 for k in range(9):i=k//3;j=k%3;g[j][6-i]=g[2-i][~j]=g[i][j]
 return g