r=range
p=lambda g:(
 h:=len(g),
 w:=len(g[0]),
 m:=[[2]+v+[2]for v in [[2]*w,*g,[2]*w]],
 n:=[*zip(*m)],
 d:=sorted([((a:=m[y][x:].index(2))*(b:=n[x][y:].index(2)),[(y+q-1,x+p-1)for p in r(a)for q in r(b)])
  for x in r(1,w+1)for y in r(1,h+1) if m[y-1][x]==m[y][x-1]==2 and m[y][x]==0
 ]),
 c:={d[0][0]:8,d[-1][0]:1},
 s:=dict(sum([[(p,c[s])for p in v] for s,v in d if s in c],[])),
 [[s[p]if(p:=(y,x))in s else g[y][x] for x in r(w)]for y in r(h)]
)[-1]