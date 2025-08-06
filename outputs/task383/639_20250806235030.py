def p(g):
 H=[]
 for i in range(len(g)):
  for j in range(len(g[0])):
   for k in range(i+2,len(g)):
    for l in range(j+2,len(g[0])):
     h=[u[j:l+1]for u in g[i:k+1]]
     C=set(sum(h,[]))
     if len(C)==1 and 0 not in C:
      H.append(((k+1-i)*(l+1-j),i,j,k,l,g[i-1][j-1],*C))
 _,i,j,k,l,b,c=max(H)
 h=[[*v]for v in g]
 for I in range(len(g)):
  if sum(v==c for v in g[I])>l+1-j:
   h[I]=[c]*(j-2)+[b]*(l+5-j)+[c]*(len(g[0])-l-2)
 g=[*map(list,zip(*g))];h=[*map(list,zip(*h))];i,j,k,l=j,i,l,k
 for I in range(len(g)):
  if sum(v==c for v in g[I])>l+1-j:
   h[I]=[c]*(j-2)+[b]*(l+5-j)+[c]*(len(g[0])-l-2)
 return [*map(list,zip(*h))]