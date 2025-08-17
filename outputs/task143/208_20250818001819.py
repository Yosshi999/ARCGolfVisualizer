def p(g):
 G=sum(g,[])
 for c in sorted(G,key=G.count):
  for k in range(1,64):
   if all(s*(w==c)+(s<1>w)for v,t in zip(g[k//8:],g[:3])for w,s in zip(v[k%8:],t[:3])):return[[(w,5)[w==c]for w in v]for v in g]