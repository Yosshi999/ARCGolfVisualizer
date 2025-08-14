e=enumerate
r=range
def D(g,y,x):
 if not(0<=y<len(g) and 0<=x<len(g[0])and(c:=g[y][x])):return[]
 t=[(y,x,c)];g[y][x]=0
 for a in r(9):t+=D(g,y+a%3-1,x+a//3-1)
 return t
def p(g):
 s=[]
 for y,v in e(g):
  for x,a in e(v):
   if len(v:=D(g,y,x))<4:
    for y,x,c in v:g[y][x]=c
   else:s+=[v]

 for d in s:
  B=max(v:=[a[2]for a in d],key=v.count)
  for k in r(8):
   for Y in r(-(H:=len(g))-5,H+5):
    for X in r(-(W:=len(g[0]))-5,W+5):
     if all([0<=(q:=y+Y)<H and 0<=(p:=x+X)<W and g[q][p]==c for y,x,c in d if c-B]):
      for y,x,c in d: g[y+Y][x+X]=c
   d=[(H-x,y,c)for y,x,c in d]
   if k==3:d=[(H-y,x,c)for y,x,c in d]

 return g