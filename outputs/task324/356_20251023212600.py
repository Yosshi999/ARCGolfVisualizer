e=enumerate
def p(g):
 W=len(g[0]);G=sum(g,[]);C=sorted(G,key=G.count)[:2];m=[];t={}
 for z,a in e(G):
  s=[G[Z+z]for Z in[-1,-W,1,W][z%W<1:]if-1<z+Z<len(G)]
  if a in C:
   t|={a:s+t.get(a,[])}
   m+=z//W+z%W,z%W-z//W-W
 u={max(t[k],key=t[k].count):k for k in t}|{k:k for k in t}
 return[[({y+x,x-y-W}&{*m}>set())*u[a]or a for x,a in e(v)]for y,v in e(g)]