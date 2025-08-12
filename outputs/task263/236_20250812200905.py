def p(g):
 G={}
 for i in range(0,len(g),3):
  for j in range(0,len(g[0]),3):
   h=[r[j:j+3]for r in g[i:i+3]]
   H=tuple(tuple(v>0 for v in u)for u in h)
   if H not in G:G[H]=[]
   G[H]+=[h]
 return G[min(G,key=lambda k:len(G[k]))][0]