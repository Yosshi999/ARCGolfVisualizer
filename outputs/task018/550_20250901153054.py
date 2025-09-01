e=enumerate
r=range
def p(g):
 H=len(g);W=len(g[0]);G=sum(g,[]);L=len(G)
 def D(z):
  if L>z>=0<(c:=G[z]):G[z]=0;return sum((D(z+a)for a in[-W,-min(1,z%W),1,W]),[(z,c)])
  return[]
 s=[]
 for z in r(L):
   if len(v:=D(z))<4:
    for z,c in v:G[z]=c
   else:s+=[v]
 for d in s:
  B=max(v:=[a[1]for a in d],key=v.count)
  for k in r(8):
   for Z in r(-L,L):
    if all(0<=z+Z<L>G[z+Z]==c for z,c in d if c-B):
      for z,c in d:G[z+Z]=c
   O=min(z//W for z,_ in d)
   d=[(((H-2*(z%W))*(k!=3)+(z%W))*W+z//W-O,c)for z,c in d]
 return[*zip(*[iter(G)]*W)]