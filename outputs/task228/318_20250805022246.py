r=range(10)
def f(g):
 c=max(set(h:=sum(g,[]))-{0},key=h.count);f=0
 for I in r:
  for J in r:
   d=g[I][J]
   if d not in[0,c]and g[I][J-1]==c:g[I][J]=0;f=1;break
  if f:break
 for i in r:
  for j in r:
   if g[i-1][j-2:j]==[c,c]and(g[i-2][j-1]==c):g[i][j]=d
 return[*map(list,zip(*g[::-1]))]
p=lambda g:f(f(f(f(g))))