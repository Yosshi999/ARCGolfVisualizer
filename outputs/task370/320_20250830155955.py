e=enumerate
R=range(1,9)
def p(g):
 C=sum(set(sum(g,[])))-g[0][0];F=lambda y,x:len(g)>y>=0<=x<len(g[0])>g[y][x]<1;y=[C in v for v in g].index(1);x=g[y].index(C)
 for k in R:
  for Y,X in(k,-k),(-k,k),(k,k),(-k,-k):
   if F(y+Y,x+X):q,p=Y,X
 for k in R:g=[[a+F(y+q*k,x+p*k)*(C-a)for x,a in e(v)]for y,v in e(g)]
 return g