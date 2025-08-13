e=enumerate
r=range
l=lambda v:(b:=0,[b:=b*2+(a>0)for a in v],b)[2]
cut=lambda g:[*map(list,zip(*[v for v in g if any(v)]))]
def p(g):
 w=len(g[0])
 t=[]
 for x in r(w-2):
  c=[]
  for y,v in e(g):
   if sum(c:=c[-6:]+v[x:x+3])!=18 and l(c)==511:g=[[0 if 0<=y-q<4 and 0<=p-x<4 else a for p,a in e(v)]for q,v in e(g)];t+=[(c.count(2),c)]
 g=cut(cut(g))
 for _,d in sorted(t)[::-1]:
  c=[d[:3],d[3:6],d[6:9]]
  for _ in'....':
   k=l(sum([[a==2 for a in v]for v in c],[]))^511
   for x,_ in e(g[0][:-2]):
    b=[]
    for y,v in e(g):
     b=b[-6:]+v[x:x+3]
     if l(b)==k:
      for i in r(9):g[y-2+i//3][x+i%3]=c[i//3][i%3]
   c=[*zip(*c)][::-1]
 return g