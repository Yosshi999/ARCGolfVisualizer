def p(g):
 h=[v[:3]for v in g[:3]];G=sum(g,[])
 for c in sorted(G,key=G.count):
  for k in range(1,64):
   i=k//8;j=k%8
   if all((s>0and w==c)or(s<1and w!=c)for v,t in zip(g[i:],h)for w,s in zip(v[j:],t)):return[[5if w==c else w for w in v]for v in g]