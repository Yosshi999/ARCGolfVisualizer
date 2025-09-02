def p(g):
 G=sum(g,[]);W=10
 D=lambda z,b:100>z>=0<(c:=G[z])and sum((D(z+a,b)for a in[-1,-W,min(1,-~z%W),W][z%W<1:G.__setitem__(z,0)]),[z-b])or[]
 s=[*map(D,R:=range(100),R)]
 for Z in R:
  for z in s[Z]:G[z+Z]=3-s.count(s[Z])
 return[*zip(*[iter(G)]*W)]