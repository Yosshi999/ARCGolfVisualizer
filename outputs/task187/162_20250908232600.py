def p(g):
 Q=[0];h=len(g);w=len(g[0]);L=h*w
 for i in Q:
  if g[y:=i//w][i%w]<1:g[y][i%w]=3;Q+=i-1,i-w,(i+w)%L,-~i%L,i%h*w,y
 return[[e or 2for e in v]for v in g]