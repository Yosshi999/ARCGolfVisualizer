e=enumerate
f=lambda g:[(t:=0,[(t*2|c,t:=(c==2 and 8 in v[x:])or(t and c!=8))[0]for x,c in e(v)])[1]for*v,in zip(*g)][::-1]
def p(g):
 t=f(f(f(f(g))))
 for y,v in e(t):
  for x,c in e(v):
    for k in range(9*(c>9)):t[y+k//3-1][x+k%3-1]={4:2}.get(k,8)
 return t