r=range(2,13)
def p(g):
 for i in r:
  for j in r:g[i][j]*=1-.25*(g[i-2][j]*g[i+2][j]*g[i][j-2]*g[i][j+2]<2)
 return [[(a,1+5*(a>1))[6in w+v]for*w,a in zip(*g,v)]for v in g]