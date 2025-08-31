e=enumerate
def f(g):
 for y,v in e(g):
  for x,_ in e(v):
   d=sum([w[x:x+3:2]for w in g[y:y+3:2]],[]);Y=y
   if 0<all(d)<len(d)>2>d.count(d[3]):
    while x>0<Y:x-=1;Y-=1;g[Y][x]=d[3]
 return[*map(list,zip(*g))][::-1]
p=lambda g:f(f(f(f(g))))