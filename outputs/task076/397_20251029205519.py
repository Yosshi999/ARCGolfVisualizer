e=enumerate
def p(g):
 G=[zip(v,v)for v in g]
 for D in[G:=[(d:=0)or[(max(d>1,((d*m>0)|m%2|(n>1<(d:=c)))*2),m)for c,m in v[::2*(n%4<1)-1]]for v in zip(*G)]for n in range(32)][-8:]:
  for Y,u in e(g):
   for X,_ in e(u):
    for y,v in e(D*all(c//2<=(g[y%len(g)-Y][x%len(g[0])-X]==m*(1-m%2))for y,v in e(D)for x,(c,m)in e(v))):
     for x,(c,m)in e(v):g[y%len(g)-Y][x%len(g[0])-X]|=c//2*m
 return g