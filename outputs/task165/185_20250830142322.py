def p(g):
 v=sum(g,[])
 C=min(c for x,c in enumerate(v)if v[x:x+3]==[c]*3!=v.count(c)==10)
 return[*zip(*(v[:(b:=-v[::-1].index(C))]+(max(v[b:]),)*20if C in v else v for v in zip(*g)))]