e=enumerate
def p(g):
 for _ in'_'*4:g=[(t:=0)or[(t*2|w,t:=(w==2)*(8in v[j:])or(t*w!=t*8))[0]for j,w in e(v)]for*v,in zip(*g)][::-1]
 for i,v in e(g):
  for j,w in e(v):
    for k in range(9*(w>9)):g[i+k//3-1][j+k%3-1]=2+(k!=4)*6
 return g