def p(g):
 G={}
 for i in range(0,len(g),3):
  for j in range(0,len(g[0]),3):h=[r[j:j+3]for r in g[i:i+3]];H=(*[(*[w>0for w in v],)for v in h],);G[H]=G.get(H,[])+[h]
 return G[min(G,key=lambda k:len(G[k]))][0]