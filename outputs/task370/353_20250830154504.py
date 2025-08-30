e=enumerate
def p(g):
 b=g[0][0];c=sum(set(sum(g,[])))-b
 F=lambda y,x:len(g)>y>=0<=x<len(g[0])and g[y][x]==0
 y=[c in v for v in g].index(1)
 x=g[y].index(c)
 for k in range(9):
  for q,p in(k,-k),(-k,k),(k,k),(-k,-k):
   if F(y+q,x+p):
    d=[q,p]
 for k in range(1,9):
  g=[[c if F(y+d[0]*k,x+d[1]*k) else a for x,a in e(v)]for y,v in e(g)]
 return g