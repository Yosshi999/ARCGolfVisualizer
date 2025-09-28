def p(g):
 for c in{*sum(g,[])}-{0,5}:
  q=[[5*(x!=c)for*w,x in zip(*g,v)if c in w]for v in g if c in v]
  h=len(q)
  w=len(q[0])
  for i in range(9-h):
   for j in range(9-w):
    if g[i][j:j+w+2]==g[i+h+1][j:j+w+2]==[5]*(w+2) and all(g[i+1+k][j:j+w+2]==[5,*q[k],5]for k in range(h)):
     g=eval(str(g).replace(*f'{c}0'))
     for x in range(h):
      for y in range(w):g[i+1+x][j+1+y]=g[i+1+x][j+1+y]or c
 return g