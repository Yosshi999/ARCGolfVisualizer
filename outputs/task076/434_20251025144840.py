def p(g):
 G=[zip(v,v)for v in g]
 for D in[G:=[(d:=0)or[(max(d>1,((d*m>0)|m%2|(n>1<(d:=c)))*2),m)for c,m in v[::2*(n%4<1)-1]]for v in zip(*G)]for n in range(32)][-8:]:
  for Y in range(len(g)):
   for X in range(len(g[0])):
    for y,v in enumerate(D*all(c//2<=(g[y%len(g)-Y][x%len(g[0])-X]==m*(1-m%2))for y,v in enumerate(D)for x,(c,m)in enumerate(v))):
     for x,(c,m)in enumerate(v):g[y%len(g)-Y][x%len(g[0])-X]|=c//2*m
 return g