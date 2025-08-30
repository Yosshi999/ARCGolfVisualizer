r=range
def p(g):
 H=r(len(g)-2);W=r(len(g[0])-2);T=r(3)
 for i in H:
  for j in W:
   G=sum(Q:=[u[j:j+3]for u in g[i:i+3]],[])
   if g[i+1][j+1]>0<(G.count(0)in{6,4})<2<len(set(G)):
    for y in H:
     for x in W:
      if any(all([g[y+Y][x+X]==c or c!=Q[Y][X] for Y in T for X in T]) for c in G if c!=0):
       for u in T:
        for v in T:g[y+u][x+v]=Q[u][v]
 return g