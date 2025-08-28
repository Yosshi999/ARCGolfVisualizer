e=enumerate
def p(g):
 f=sum(g,L:=[]);y,x=sorted({*f}-{0},key=f.count)
 for i,v in e(g):
  for j,w in e(v):
   I=i;J=j
   while I<len(g)and g[I][j]==x:I+=1
   while J<len(v)and v[J]==x:J+=1
   L+=[[y*(w>0)for w in v[j:J]]for v in g[i:I]],
 return max(L)