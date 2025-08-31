def p(g,i=0):
 H=len(g);W=len(g[0]);G=sum(g,[])
 if i+2>H*W:return(0,g)[G.count(5)<1]
 def f(b,v,y):
  a=5;o=[*map(list,g)]
  if b:
   for j in v:a&=G[j];o[j//W][j%W]=y
   if a and(r:=p(o,i+1)):return r
  return[]
 return f(i//W+1<H>0<i%W+1<W,[i,i+1,i+W,i+W+1],8)or f(i%W+2<W,[i,i+1,i+2],2)or f(i//W+2<H,[i,i+W,i+W+W],2)or p(g,i+1)