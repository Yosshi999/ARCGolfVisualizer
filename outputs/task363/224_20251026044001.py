R=range(121)
def p(g):
 G=[5]*11
 for v in g:G+=v+[5]
 G=[G[z]or 2*any(G[z-Z]==2 and all((G[a-Z]==2)<=(G[a]==0)for a in R)and (not(Z in [23,51,79]*(G[40]==0)))for Z in R)for z in R]
 return[G[y*11:][:10]for y in range(1,11)]