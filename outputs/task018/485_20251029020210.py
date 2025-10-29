e=enumerate
r=range
def p(g):
 H=len(g);W=len(g[0]);G=*Q,=sum(g,[]);L=H*W;D=lambda T,z:L>z>=0<(c:=T[z])and sum((D(T,z+a)for a in[-1,-W,W,1][z%W<1:exec('T[z]=0')]),[(z,c)])or[]
 for d in[D(G,z)for z in r(L)if len(D(Q,z))>3]:
  B=max(v:=[a[1]for a in d],key=v.count)
  for k in r(8):
   for Z in r(-L,L):
    if all(0<=z+Z<L>G[z+Z]==c for z,c in d if c-B):
     for z,c in d:G[z+Z]=c
   d=[(((H-z%W*2)*(k!=3)+z%W)*W+z//W-min(z//W for z,_ in d),c)for z,c in d]
 return[*zip(*[iter(G)]*W)]