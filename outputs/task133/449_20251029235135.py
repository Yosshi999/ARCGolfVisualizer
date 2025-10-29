e=enumerate
def p(g):
 S={(i,j):w for i,v in e(g)for j,w in e(v)if w}
 t=[]
 o=[]
 def f(h):
  if h in S:L[h]=S.pop(h);A,B=h;f((A-1,B));f((A+1,B));f((A,B-1));f((A,B+1))
 while S:o+=[L:={}];f(min(S))
 for r in o+o:
  d,={*o[0].values()}&{*o[1].values()};c,={*r.values()}-{d};x,y=min(z:=[u for u in r if r[u]==d]);b=max(z)[0]+1-x;t+=[(u[0]-x,u[1]-y)for u in r if(r[u]==c)==b]
  for i,j in t:
   for k in range(b*b):g[x+i*b+k//b][y+j*b+k%b]=c
 return g