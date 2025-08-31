r=range
F=lambda g:[[*v]for v in zip(*g)if any(v)]
def p(g):
 t=[]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   c=[v[x:x+3]for v in g[y:y+3]]
   if sum(s:=sum(c,[]))!=18>0<all(s):
    for Y in r(3):
     for X in r(3):g[y+Y][x+X]=0
    t+=(s.count(2),c),
 g=F(F(g))
 for _,c in sorted(t)[::-1]:
  for _ in'....':
   for y in r(len(g)-2):
    for x in r(len(g[0])-2):
     if all((c[Y][X]==2 and g[y+Y][x+X]==0)or(c[Y][X]!=2 and g[y+Y][x+X]==2)for Y in r(3) for X in r(3)):
      for Y in r(3):
       for X in r(3):g[y+Y][x+X]=c[Y][X]
   c=[*zip(*c)][::-1]
 return g