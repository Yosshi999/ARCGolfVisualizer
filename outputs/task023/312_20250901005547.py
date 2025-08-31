def p(g,i=0):
 H=len(g);W=len(g[0]);G=sum(g,[])
 if i+2>H*W:return(0,g)[G.count(5)<1]
 def f(y,*v):
  a=5;o=[*map(list,g)]
  for k in v:j=i+k;a&=G[j];o[j//W][j%W]=y
  return r if a and(r:=p(o,i+1))else[]
 return(i<H*W-W>0<i%W<W-1and f(8,0,1,W,W+1))or(i%W<W-2and f(2,0,1,2))or(i//W<H-2and f(2,0,W,W+W))or p(g,i+1)