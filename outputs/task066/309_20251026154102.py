def f(g,q,p,y,x,d=3):
 if-1<y+q<len(g)>x+p>=0<d:
  if(t:=g[y+q][x+p])>7:return f(g,p:=p&1,q:=q&1,y,x,d-1)or f(g,-p,-q,y,x,d-1)
  if t==2:return g
  g=eval(str(g));g[y+q][x+p]=3;return f(g,q,p,y+q,x+p,d)
p=lambda g,z=0:f(g,D:=g[y+1][x]%2,1-D,y,x)or f(g,-D,D-1,y,x)if g[y:=z//len(g)][x:=z%len(g)]%2else p(g,z+1)