r=range(10)
e=enumerate
f=lambda g:max((d*(sum((v[x::d][:2]for v in g[y::d][:2]),[])==[g[y][x]]*4)*(g[y][x]>0),x-y,x+y+d,x,y) for d in r[1:] for x in r for y in r)
p=lambda g:(d:=f(g),[[(c:=a,x:=r,y:=s,[(c:=c|g[(y+10)%10][(x+10)%10],t:=y,y:=d[2]-x,x:=t+d[1])for _ in'....'],c)[-1] for r,a in e(v)]for s,v in e(g)],[d])[-2]