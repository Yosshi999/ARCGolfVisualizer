r=range
e=enumerate
t=lambda g:[*map(list,zip(*g))][::-1]
f=lambda s,g:(
 [(c:=0,w:=0,[w:=(w if (c:=c+sum(g[y][t:b+1])) else y) for y in r(30)],s:=s+([((b-t+6)*w,(-1,w+(w==29),t,b))] if w else [])) for t in r(31) for b in r(31) if b>t+2],
 s:=[(s,(29-r,29-l,u,d)) for s,(u,d,l,r) in s],
 (s,t(g))
 )[-1]
h=lambda g:t([(w:=v,[w:=[3]*x+v[x:]for x in r(30) if v[x]==3 and all(v[:x]==[0]*x for v in g[max(0,y-1):y+2])],w)[2] for y,v in e(g)])
p=lambda g:(
 s:=f(*f(*f(*f([],g)))),
 p:=sorted(s[0])[-1][1],
 g:=[[3 if p[0]<y<p[1] and p[2]<x<p[3] else a for x,a in e(v)]for y,v in e(g)],
 h(h(h(h(g))))
)[-1]