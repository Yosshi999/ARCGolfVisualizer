r=range(31)
e=enumerate
t=lambda g:[*map(list,zip(*g))][::-1]
def h(g):
 for y,v in e(g):
  x=bytes(v).find(3)
  if all({*v[:x]}<={0,3}for v in g[y-(y>0):y+2]):v[:x]=[3]*x
 return t(g)
def p(g):s=[];exec('''for a in r:
 for b in r[a+3:]:
  w=0
  while~-any(g[w+1][a:b+1])and 28>w:w+=1
  s+=[((b-a+6)*w,(-1,w+(w==29),a,b))]
s[:]=[(s,(29-r,29-l,u,d))for s,(u,d,l,r)in s]
g=t(g)
'''*4);u,d,l,R=sorted(s)[-1][1];return h(h(h(h([[3*(u<i<d)*(l<j<R)or w for j,w in e(v)]for i,v in e(g)]))))