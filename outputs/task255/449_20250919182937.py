r=range(31)
e=enumerate
t=lambda g:[*zip(*g)][::-1]
h=lambda g:t([(v,[3]*(j:=bytes(v).find(3))+v[j:])[all({*u[:j]}<={0,3}for u in g[i-(i>0):i+2])]for i,(*v,)in e(g)])
def p(g):s=[];exec('''for a in r:
 for b in r[a+3:]:
  w=0
  while~-any(g[w+1][a:b+1])and 28>w:w+=1
  s+=((b-a+6)*w,(-1,w,a,b)),
s[:]=[(s,(29-r,29-l,u,d))for s,(u,d,l,r)in s]
g=t(g)
'''*4);u,d,l,R=max(s)[1];return h(h(h(h([[3*(u<i<d)*(l<j<R)or w for j,w in e(v)]for i,v in e(g)]))))