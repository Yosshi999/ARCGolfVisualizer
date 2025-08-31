def p(g,i=0):
 H=len(g);W=len(g[0]);G=sum(g,[])
 if i+2>H*W:return(0,g)[G.count(5)<1]
 def f(b,y,*v):
  a=5;o=[*map(list,g)]
  if b:
   for k in v:j=i+k;a&=G[j];o[j//W][j%W]=y
  return r if(a*b)and(r:=p(o,i+1))else[]
 return f(i//W+1<H>0<i%W+1<W,8,0,1,W,W+1)or f(i%W+2<W,2,0,1,2)or f(i//W+2<H,2,0,W,W+W)or p(g,i+1)