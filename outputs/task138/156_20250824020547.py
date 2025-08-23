def p(g,d=8):
 c=0;g=[v if d>4else v[:(x:=v.index(C:=v[-1]))]+[C]*(len(v)-x)for v in g if(c:=c|all(v))]
 return p([*map(list,zip(*g))][::-1],d-1)if d else g