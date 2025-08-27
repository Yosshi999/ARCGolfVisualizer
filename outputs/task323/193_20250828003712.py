def f(g):
 i,j=divmod(sum(g,[]).index(8),13)
 for _ in[0]*9:
  for x,y in(-1,0),(-1,0),(0,1),(0,1):
   i+=x;j+=y
   if 13>i>-1<j<13:g[i][j]=5
 return[v[::-1]for v in g[::-1]]
p=lambda g:f(f(g))