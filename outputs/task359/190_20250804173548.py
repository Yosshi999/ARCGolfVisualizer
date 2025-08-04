f=lambda x:[[max(v,key=v.count)]*len(v)for v in x]
F=lambda x:[*map(list,zip(*x))]
def p(g):
 h=f(g)
 i=F(f(F(g)))
 return min(h,i,key=lambda x:sum(v!=w for v,w in zip(sum(g,[]),sum(x,[]))))