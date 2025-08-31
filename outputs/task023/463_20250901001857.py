def p(g,i=0):
 H=len(g);W=len(g[0]);G=sum(g,[]);f=lambda g:[*map(list,g)];y=i//W;x=i%W
 if i+2>H*W:return(0,g)[G.count(5)<1]
 if y+1<H>0<x+1<W>5==G[i]&G[i+1]&G[i+W]&G[i+W+1]:
  o=f(g)
  for j in 0,1,2,3:o[y+j//2][x+j%2]=8
  if(r:=p(o,i+1)):return r
 if x+2<W>5==G[i]&G[i+1]&G[i+2]:
  o=f(g)
  for j in 0,1,2:o[y][x+j]=2
  if(r:=p(o,i+1)):return r
 if y+2<H>5==G[i]&G[i+W]&G[i+W+W]:
  o=f(g)
  for j in 0,1,2:o[y+j][x]=2
  if(r:=p(o,i+1)):return r
 return p(g,i+1)