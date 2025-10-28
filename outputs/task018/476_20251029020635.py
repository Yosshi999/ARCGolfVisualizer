e=enumerate
r=range
def p(g):
 H=len(g);W=len(g[0]);G=*Q,=sum(g,[]);L=H*W;D=lambda T,z:L>z>=0<(c:=T[z])and sum((D(T,z+a)for a in[-1,-W,W,1][z%W<1:exec('T[z]=0')]),[(z,c)])or[]
 for u in r(L):
  if len(D(Q,u))>3:
   d=D(G,u);B=max(v:=[a[1]for a in d],key=v.count)
   for k in r(8):
    for Z in r(-L,L):
     for z,c in all(c==G[(z+Z)%L]for z,c in d if c-B)*d:G[(z+Z)%L]=c
    d=[(((H-z%W*2)*(k!=3)+z%W)*W+z//W-min(z//W for z,_ in d),c)for z,c in d]
 return[*zip(*[iter(G)]*W)]