def p(g):
 h=sum(g,[])
 c=min(h,key=h.count)
 return[v[v.index(c):len(v)-v[::-1].index(c)]for v in g if c in v]