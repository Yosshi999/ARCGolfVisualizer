e=enumerate
def p(g):
 f=sum(g,[]);y,x=sorted({*f}-{0},key=f.count);L=[]
 for i,v in e(g):
  for j,w in e(v):
   I=i;J=j
   while I<len(g)and g[I][j]==x:I+=1
   while J<len(v)and v[J]==x:J+=1
   L+=[v[j:J]for v in g[i:I]],
 return[[y*(w>0)for w in v]for v in max(L)]