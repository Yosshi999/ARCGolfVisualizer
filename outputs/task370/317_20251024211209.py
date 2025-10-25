e=enumerate
R=range(1,9)
def p(g):
 C=sum(set(u:=sum(g,[])))-(w:=g[0])[0];F=lambda y,x:len(g)>y>=0<=x<len(g[0])>g[y][x]<1;v=u.index(C);y,x=v//len(w),v%len(w);q,p=[(Y,X)for k in R for Y,X in[(k,-k),(-k,k),(k,k),(-k,-k)]if F(y+Y,x+X)][-1]
 for k in R:g=[[a+F(y+q*k,x+p*k)*(C-a)for x,a in e(v)]for y,v in e(g)]
 return g