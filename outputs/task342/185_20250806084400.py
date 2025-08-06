def f(g):
 for k in range(100):
  if g[i:=k//10][j:=k%10]==8:
   m=0
   for v in g[:i]:m=max(m,*v[:j]);v[:j]=[0]*j
   g[i][j]=m;return[*map(list,zip(*g[::-1]))]
p=lambda g:f(f(f(f(g))))