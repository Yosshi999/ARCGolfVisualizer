e=enumerate
R=range(1,9)
def p(g):
 w=g[0];u=sum(g,[]);F=lambda y,x:len(g)>y>-1<x<len(g[0])>g[y][x]<1;y,x=divmod(u.index(C:=sum({*u})-w[0]),len(w));q,p=[(Y,X)for k in R for Y,X in[(k,-k),(-k,k),(k,k),(-k,-k)]if F(y+Y,x+X)][-1]
 for k in R:g=[[(a,C)[F(y+q*k,x+p*k)]for x,a in e(v)]for y,v in e(g)]
 return g