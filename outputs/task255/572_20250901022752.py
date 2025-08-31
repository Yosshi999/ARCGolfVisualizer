r=range
e=enumerate
t=lambda g:[*map(list,zip(*g))][::-1]
h=lambda g:t([(w:=v,[w:=[3]*x+v[x:]for x in r(30) if v[x]==3 and all(v[:x]==[0]*x for v in g[max(0,y-1):y+2])],w)[2] for y,v in e(g)])
def p(g):
 s=[]
 for _ in"....":
  for a in r(31):
   for b in r(a+3,31):
    c=w=0
    for y in r(30):
     w=(w if (c:=c+sum(g[y][a:b+1])) else y)
    s+=([((b-a+6)*w,(-1,w+(w==29),a,b))] if w else [])
  s=[(s,(29-r,29-l,u,d)) for s,(u,d,l,r) in s]
  g=t(g)
 p=sorted(s)[-1][1]
 g=[[3 if p[0]<y<p[1] and p[2]<x<p[3] else a for x,a in e(v)]for y,v in e(g)]
 return h(h(h(h(g))))