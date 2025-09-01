e=enumerate
r=range
def p(g):
 H=len(g);W=len(g[0])
 def D(y,x):
  if H>y>-1<x<W>0<(c:=g[y][x]):g[y][x]=0;return sum((D(y+a%3-1,x+a//3-1)for a in r(9)),[(y,x,c)])
  return[]
 s=[]
 for y in r(H):
  for x in r(W):
   if len(v:=D(y,x))<4:
    for y,x,c in v:g[y][x]=c
   else:s+=[v]
 for d in s:
  B=max(v:=[a[2]for a in d],key=v.count)
  for k in r(8):
   for Y in r(-H-5,H+5):
    for X in r(-W-5,W+5):
     if all([0<=(q:=y+Y)<H and 0<=(p:=x+X)<W and g[q][p]==c for y,x,c in d if c-B]):
      for y,x,c in d: g[y+Y][x+X]=c
   d=[((H-2*x)*(k!=3)+x,y,c)for y,x,c in d]
 return g