e=enumerate
r=range
F=lambda g:[[*v]for v in zip(*g)if any(v)]
def p(g):
 W=len(g[0]);t=[]
 for x in r(W-2):
  c=[]
  for y,v in e(g):
   if sum(c:=c[-6:]+v[x:x+3])!=18 and all(c) and len(c)==9:
    for Y in r(3):
     for X in r(3):
      g[y-Y][x+X]=0
    t+=[(c.count(2),c)]
 g=F(F(g))
 for _,d in sorted(t)[::-1]:
  c=[d[:3],d[3:6],d[6:9]]
  for _ in'....':
   for y in r(len(g)-2):
    for x in r(len(g[0])-2):
     if all((c[Y][X]==2 and g[y+Y][x+X]==0) or (c[Y][X]!=2 and g[y+Y][x+X]==2) for Y in r(3) for X in r(3)):
      for Y in r(3):
       for X in r(3):g[y+Y][x+X]=c[Y][X]
   c=[*zip(*c)][::-1]
 return g