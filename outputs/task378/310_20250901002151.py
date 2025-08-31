e=enumerate
def f(g):
 t=[]
 for y,v in e(g):
  for x,_ in e(v):
   d=sum([w[x:x+3:2]for w in g[y:y+3:2]],[])
   if 0<all(d)<len(d)>2>d.count(b:=d[0]):
    t+=[(y+k+3,x+k+3)for k in range(9)]
 g=[[b if(y,x)in t else a for x,a in e(v)]for y,v in e(g)]
 return [*map(list,zip(*g))][::-1]
p=lambda g:f(f(f(f(g))))