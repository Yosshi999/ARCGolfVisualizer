def p(g):
 for d in 1,-1:
  u=g.index(v:=max(g));v=v.index(8)
  for x,y in([(-d,0)]*2+[(0,d)]*2)*9:
   u+=x;v+=y
   if 13>u>-1<v<13:g[u][v]=5
 return g