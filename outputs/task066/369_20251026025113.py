e=enumerate
def f(g,q,p,y,x,d=3):
 g=eval(str(g))
 if d>0<len(g)>y+q>-1<x+p<len(g[0]):
  if(t:=g[y+q][x+p])>7:return f(g,p:=p&1,q:=q&1,y,x,d-1)or f(g,-p,-q,y,x,d-1)
  if t==2:return g
  g[y+q][x+p]=3;return f(g,q,p,y+q,x+p,d)
p=lambda g:[f(g,D:=g[y+1][x]==3,1-D,y+D,x+1-D)or f(g,-D,D-1,y,x)for y,v in e(g[:-1])for x,a in e(v[:-1])if a==3and 3in[g[y+1][x],g[y][x+1]]][0]