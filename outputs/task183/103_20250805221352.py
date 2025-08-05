def p(g):
 n=len(g);r=range(2,n-2)
 return[[g[2*i//n*~-n][2*j//n*~-n]*(g[i][j]>0)for j in r]for i in r]