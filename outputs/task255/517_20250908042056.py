r=range
e=enumerate
t=lambda g:[*map(list,zip(*g))][::-1]
def h(g):
 Q=[]
 for y,v in e(g):
  if 3 in v:
   x=v.index(3)
   if all(v[:x]==[0]*x for v in g[max(0,y-1):y+2]):v=[3]*x+v[x:]
  Q+=v,
 return t(Q)
def p(g):s=[];exec('''for a in r(31):
 for b in r(a+3,31):
  w=0
  while~-any(g[w+1][a:b+1])and 28>w:w+=1
  s+=[((b-a+6)*w,(-1,w+(w==29),a,b))]
s[:]=[(s,(29-r,29-l,u,d))for s,(u,d,l,r)in s]
g=t(g)
'''*4);u,d,l,R=sorted(s)[-1][1];return h(h(h(h([[3 if u<y<d and l<x<R else a for x,a in e(v)]for y,v in e(g)]))))