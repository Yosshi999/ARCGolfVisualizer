e=enumerate
r=range
def p(g):
 H=len(g);W=len(g[0]);G=sum(g,s:=[]);L=H*W;D=lambda z:L>z>=0<(c:=G[z])and sum((D(z+a)for a in[-1,-W,W,1][z%W<1:exec('G[z]=0')]),[(z,c)])or[]
 for z in r(L):
  if len(v:=D(z))<4:
   for z,c in v:G[z]=c
  else:s+=v,
 for d in s:
  B=max(v:=[a[1]for a in d],key=v.count)
  for k in r(8):
   for Z in r(-L,L):
    if all(0<=z+Z<L>G[z+Z]==c for z,c in d if c-B):
     for z,c in d:G[z+Z]=c
   d=[(((H-z%W*2)*(k!=3)+z%W)*W+z//W-min(z//W for z,_ in d),c)for z,c in d]
 return[*zip(*[iter(G)]*W)]