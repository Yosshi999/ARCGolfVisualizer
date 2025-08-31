e=enumerate
def f(g):
 for y,v in e(g):
  for x,_ in e(v):
   d=sum([w[x:x+3:2]for w in g[y:y+3:2]],[])
   if 0<all(d)<len(d)>2>d.count(d[3]):
    for k in range(1,10):
     if(Y:=y-k)>=0<=(X:=x-k):g[Y][X]=d[3]
 return[*map(list,zip(*g))][::-1]
p=lambda g:f(f(f(f(g))))