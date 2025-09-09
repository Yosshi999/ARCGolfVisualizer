def p(g):
 Q=[0];w=len(g[0])
 for i in Q:
  if g[y:=i//w][i%w]<1:g[y][i%w]=3;Q+=i-1,i-w,i+w,-~i,i%len(g)*w,y
 return[[e or 2for e in v]for v in g]