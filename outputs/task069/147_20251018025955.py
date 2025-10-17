def p(g):
 for Z,_ in(E:=[*enumerate(G:=sum(g,i:=[]))]):
  for z,c in(G[Z]==8)*E:
   if c&7:i+=z,;G[z]=0;G[Z+z-i[0]]=c
 return[*zip(*[iter(G)]*10)]