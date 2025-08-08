def t(g,i,J):
 for j in J:
  if g[0][j]==2:i+=1
  if g[-1][j]==2:i-=1
  if 0<=i<len(g):g[i][j]=8
def f(g,h):
 g=[*map(list,zip(*g))]
 h=[*map(list,zip(*h))]
 if 2 in g[0][1:-1] or 2 in g[-1][1:-1]:
  for i,v in enumerate(g):
   if v[0]==8:t(h,i,range(len(v)))
   if v[-1]==8:t(h,i,range(len(v)-1,-1,-1))
 return g,h
p=lambda g:f(*f(g,[[*v]for v in g]))[1]