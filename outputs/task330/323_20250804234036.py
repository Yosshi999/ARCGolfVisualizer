r=[-1,0,1]
def p(g):
 h=len(g);w=len(g[0])
 for i in range(h):
  for j in range(w):
   n=[0]
   def f(c,d):
    Q=[(i,j)]
    while Q:
     s,t=Q.pop()
     for x in r:
      for y in r:
       I=s+x;J=t+y
       if 0<=I<h*(0<=J<w)and g[I][J]==c:n[0]+=1;g[I][J]=d;Q+=(I,J),
   if g[i][j]>2:f(5,3);f(3,1+(n[0]==6))
 return g