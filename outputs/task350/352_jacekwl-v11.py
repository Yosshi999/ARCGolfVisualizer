def p(g,P=range):
 l=[r[:]for r in g]
 for c in P(1,10):
  O=[(i,j)for i in P(len(g))for j in P(len(g[0]))if g[i][j]==c]
  for i in P(len(O)):
   for j in P(i+1,len(O)):
    d,p=O[i]
    U,n=O[j]
    if d==U:
     for x in P(min(p,n),max(p,n)+1):l[d][x]=8
    elif p==n:
     for y in P(min(d,U),max(d,U)+1):l[y][p]=8
  for d,U in O:l[d][U]=1
 return l