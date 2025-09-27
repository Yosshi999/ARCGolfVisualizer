r=range(30)
t=lambda g:[*zip(*g)][::-1]
h=lambda g:t([(v:=[*g[i]],[3]*(j:=bytes(v).find(3))+v[j:])[all(sum(u[:j])<1for u in g[i-(i>0):i+2])]for i in r])
def p(g):
 s=[]
 for _ in[0]*4:
  for a in r:
   for b in r:
    w=0
    while~-any(g[w+1][a:b+1])and 28>w:w+=1
    s+=((b-a+6)*w,(-1,w,a,b)),
  s=[(s,(29-r,29-l,u,d))for s,(u,d,l,r)in s]
  g=t(g)
 u,d,l,R=max(s)[1]
 return h(h(h(h([[3*(u<i<d)*(l<j<R)or g[i][j]for j in r]for i in r]))))