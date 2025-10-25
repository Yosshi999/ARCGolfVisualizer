r=range
F=lambda g:[v for*v,in zip(*g)if any(v)]
def p(g):
 t=[]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   if sum(s:=sum(c:=[v[x:x+3]for v in g[y:y+3]],[]))^18>0<all(s):
    for v in g[y:y+3]:v[x:x+3]=[0]*3
    t+=(-s.count(2),c),
 g=F(F(g))
 for _,c in sorted(t):
  for _ in'.'*4:
   for y in r(len(g)-2):
    for x in r(len(g[0])-2):
     if all((c[Y:=Z//3][X:=Z%3]==2)==(g[y+Y][x+X]==0)for Z in r(9)):
      for Z in r(3):g[y+Z][x:x+3]=c[Z]
   c[::-1]=F(c)
 return g