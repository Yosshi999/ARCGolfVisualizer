def p(g):
 v=max(g,key=lambda x:max(x)>0)
 m=max(v)
 k=v.index(m)+(15-v[::-1].index(m))
 return[[m*(m in[v[j],v[k-j]if 0<=k-j<16else 0])for j,w in enumerate(v)]for v in g]