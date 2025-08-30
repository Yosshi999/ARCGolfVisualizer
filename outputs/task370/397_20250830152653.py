i=lambda v,k:v[k]if 0<=k<len(v)else[-1]
e=enumerate
def p(g):
 b=g[0][0];c=sum(set(sum(g,[])))-b;h=len(g)
 y=[c in v for v in g].index(1)
 x=g[y].index(c)
 d=max(filter(lambda p: 0<=p[1]+y<h and i(i(g,p[1]+y),p[2]+x)==0,[*sum((((x,x,-x),(x,-x,x),(x,x,x),(x,-x,-x))for x in range(9)),())]))
 for k in range(1,9):
  g=[[a if i(i(g,y+d[1]*k),x+d[2]*k)else c for x,a in e(v)]for y,v in e(g)]
 return g