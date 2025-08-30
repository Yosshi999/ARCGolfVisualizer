e=enumerate
def p(g):
 G=sum(g,[]);s=[v for v in e(G)if v[1]&7]
 for Z,_ in e(G):
  if G[Z]==8:
   for z,c in s:G[z]=0;G[Z+z-s[0][0]]=c
 return[*zip(*[iter(G)]*10)]