def p(g):
 h,w=len(g),len(g[0]);y,x=sorted({*sum(g,[])}-{0},key=sum(g,[]).count);L=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]==x:
    I=i;J=j
    while I<h and g[I][j]==x:I+=1
    while J<w and g[i][J]==x:J+=1
    L+=[v[j:J]for v in g[i:I]],
 return[[y*(w>0)for w in v]for v in max(L)]