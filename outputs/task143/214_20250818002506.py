def p(g):
 G=sum(g,[])
 c=[c for c in sorted(G,key=G.count)if any(all(s*(w==c)+(s<1>w)for v,t in zip(g[k//8:],g[:3])for w,s in zip(v[k%8:],t[:3]))for k in range(1,64))][0]
 return[[(w,5)[w==c]for w in v]for v in g]