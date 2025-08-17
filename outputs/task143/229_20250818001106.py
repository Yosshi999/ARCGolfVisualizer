def p(g):
 G=sum(g,[])
 for c in sorted(G,key=G.count):
  for k in range(1,64):
   i=k//8;j=k%8
   if all((s and w==c)or(s<1and w<1)for v,t in zip(g[i:],g[:3])for w,s in zip(v[j:],t[:3])):return[[(w,5)[w==c]for w in v]for v in g]