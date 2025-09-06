def p(g):
 G=*H,=sum(g,[]);w=len(g[0])
 for i,v in enumerate(G):
  if v and i+w+1<len(G)and v in G[i+w+1:]:H[i]-=v;H[i+1]+=v
 return[*zip(*[iter(H)]*w)]