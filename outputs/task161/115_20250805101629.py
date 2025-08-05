def p(g):
 c=min(h:=sum(g,[]),key=h.count)
 return[[c*(v[0]==c==v[-1]or w[0]==c==w[-1])for w in zip(*g)]for v in g]