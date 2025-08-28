def p(g):
 i=g[-2].index(g[-1][0])
 for j in range(i):v=g[-i-2+j];v[j]=v[~j]=g[-1][i]
 return g