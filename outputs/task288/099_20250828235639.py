def p(g):
 i=g[-2].index(g[-1][0])
 for j in range(i):g[-i-2+j][j]=g[-i-2+j][~j]=g[-1][i]
 return g