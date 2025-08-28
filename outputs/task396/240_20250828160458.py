e=enumerate
def p(g):
 y=min(f:=sum(g,L:=[]),key=f.count)
 for i,v in e(g):
  for j,w in e(v):
   I=i;J=j
   while I<len(g)and g[I][j]==w:I+=1
   while J<len(v)and v[J]==w:J+=1
   L+=[[y*(w>0)for w in v[j:J]]for v in g[i:I]],
 return max(L)