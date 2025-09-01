r=range
def p(g):
 W=len(g[0]);G=sum(g,[]);L=len(G)
 def D(z):
  if L>z>=0<(c:=G[z]):G[z]=0;return sum((D(z+a)for a in[-W,-min(1,z%W),min(1,(z+1)%W),W]),[c])
  return[]
 return[[8*any([1 for z in r(L)if D(z).count(2)>4])]]