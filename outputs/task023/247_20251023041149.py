def p(g,i=0):
 H=len(g);W=len(g[0]);G=sum(g,[])
 def f(y,*v):
  a=5;o=[*map(list,g)]
  for k in v:j=(i+k)%len(G);a&=G[j];o[j//W][j%W]=y
  if a:return p(o,i+1)
 return-~-(5in G)*g if H*W<i+2else f(8,0,1,W,W+1)or f(2,0,1,2)or f(2,0,W,W+W)or p(g,i+1)