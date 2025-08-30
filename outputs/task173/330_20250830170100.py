r=range
def p(g):
 W=len(g[0])-2;R=r((len(g)-2)*W);T=r(9)
 for k in R:
  j=k%W;i=k//W;G=sum(Q:=[u[j:j+3]for u in g[i:i+3]],[])
  if g[i+1][j+1]>0<(G.count(0)in{6,4})<2<len(set(G)):
   for l in R:
    y=l//W;x=l%W
    if~-all(any(g[y+z//3][x+z%3]!=c==G[z]for z in T)for c in G if c):
     for z in T:g[y+z//3][x+z%3]=G[z]
 return g