def p(g,d=44):
 m=min(g,key=lambda x:(max(x)<1,-x.count(0)));c=max(m);i=g.index(m)
 if m.count(c)==1 and c in g[i-1]:g[1:i+1]=g[:i]
 return p([*zip(*g[::-1])],d-1)if d else g