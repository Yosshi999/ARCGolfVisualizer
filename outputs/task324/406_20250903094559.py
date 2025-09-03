e=enumerate
l=lambda v,x:(v[1:][::-1]+v)[x+len(v)-2:][:3]
def p(g):
 G=sum(g,[]);C=sorted(G,key=G.count)[:2];m=[];t={}
 for y,v in e(g):
  for x,a in e(v):
   s=l(v,x)[::2]+[*l([*zip(*g)][x],y)]
   for d in range(-20,20):
    if a in C:t|={a:s+t.get(a,[])};m+=[(y-d,x-d),(y-d,x+d)]
 t={max(t[k],key=t[k].count):k for k in t}|{k:k for k in t}
 return[[t[a]if(y,x)in m else a for x,a in e(v)]for y,v in e(g)]