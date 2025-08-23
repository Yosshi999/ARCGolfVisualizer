def p(g):
 r=[[a for*w,a in zip(*g,v)if 2in w]for v in g if 2in v]
 c=max({*sum(g,[])}-{0,2})
 h=[[a for*w,a in zip(*g,v)if c in w]for v in g if c in v]
 n=len(r)-2
 b=n//3
 for i in range(n):
  for j in range(n):
   r[i+1][j+1]=h[i//b][j//b]
 return r