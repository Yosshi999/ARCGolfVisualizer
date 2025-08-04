r=[-1,0,1]
def p(g):
 h=len(g);w=len(g[c:=0])
 for i in range(h):
  for j in range(w):
   if g[i][j]:
    Q=[(i,j)];c+=1
    while Q:
     i,j=Q.pop()
     for x in r:
      for y in r:
       I=i+x;J=j+y
       if 0<=I<h*(0<=J<w)and g[I][J]:g[I][J]=0;Q+=(I,J),
 R=range(c);return[[8*(i==j)for j in R]for i in R]