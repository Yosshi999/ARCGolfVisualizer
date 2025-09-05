e=enumerate
def p(g):
 for _ in'_'*4:g=[(t:=0,[(t*2|c,t:=(8in v[x:]*(c==2))or(t*c!=t*8))[0]for x,c in e(v)])[1]for*v,in zip(*g)][::-1]
 for y,v in e(g):
  for x,c in e(v):
    for k in range(9*(c>9)):g[y+k//3-1][x+k%3-1]={4:2}.get(k,8)
 return g