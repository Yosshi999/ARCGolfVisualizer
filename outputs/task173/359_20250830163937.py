r=range
def p(g):
 H=r(len(g)-2);W=r(len(g[0])-2);T=r(9)
 for i in H:
  for j in W:
   G=sum(Q:=[u[j:j+3]for u in g[i:i+3]],[])
   if g[i+1][j+1]>0<(G.count(0)in{6,4})<2<len(set(G)):
    for y in H:
     for x in W:
      if any(all(c!=Q[Y:=Z//3][X:=Z%3]or g[y+Y][x+X]==c for Z in T)for c in G if c):
       for z in T:g[y+Y][x+X]=Q[Y:=z//3][X:=z%3]
 return g