def p(g):
 h,w=len(g),len(g[0])
 y,x=sorted({*sum(g,[])}-{0},key=sum(g,[]).count)
 L=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]==x:
    I=i
    while I<h and g[I][j]==x:I+=1
    J=j
    while J<w and g[i][J]==x:J+=1
    L.append(((I-i)*(J-j),[v[j:J]for v in g[i:I]]))
 f=max(L)[1]
 return[[y*(w>0)for w in v]for v in f]