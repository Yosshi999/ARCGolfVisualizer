R=range(29)
def p(g):
 H,*_=[K for K in R[1:]if all(a*a*b==a*b*b for(c,d)in zip(g,g[K:])for(a,b)in zip(c,d))]
 return[[max(g[I][j]for I in R[i%H::H])or j-1 for j in R]for i in R]