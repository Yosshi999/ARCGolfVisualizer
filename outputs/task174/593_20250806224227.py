def t(g,c,W):
 for i in range(10):
  for j in range(10):
   if 0<=W-j<10:
    if g[i][j]==c and g[i][W-j]!=c or g[i][j]!=c and g[i][W-j]==c:return 0
   else:
    if g[i][j]==c:return 0
 return 1 
def f(g):
 for c in range(1,10):
  if any(v==c for u in g for v in u):
   for W in range(19):
    if t(g,c,W):
     x=[j for i in range(10) for j in range(10) if g[i][j]==c]
     y=[i for i in range(10) for j in range(10) if g[i][j]==c]
     return [r[min(x):max(x)+1]for r in g[min(y):max(y)+1]]
def p(g):
 if (q:=f(g)): return q
 g=[*map(list,zip(*g))]
 if (q:=f(g)): return [*map(list,zip(*q))]