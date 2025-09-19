r=range
F=lambda g:[v for*v,in zip(*g)if any(v)]
def p(g):
 t=[]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   c=[v[x:x+3]for v in g[y:y+3]]
   if sum(s:=sum(c,[]))!=18>0<all(s):
    for Z in r(9):g[y+Z//3][x+Z%3]=0
    t+=(-s.count(2),c),
 g=F(F(g))
 for _,c in sorted(t):
  for _ in'.'*4:
   for y in r(len(g)-2):
    for x in r(len(g[0])-2):
     if all((c[Y:=Z//3][X:=Z%3]==2)==(g[y+Y][x+X]==0)for Z in r(9)):
      for Z in r(9):g[y+Z//3][x+Z%3]=c[Z//3][Z%3]
   c[::-1]=zip(*c)
 return g