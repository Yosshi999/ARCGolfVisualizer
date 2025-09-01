def p(g):
 H=len(g);W=len(g[0]);a=0
 for z in range(H*W):
  Q=[(z//H,z%H)];C=0
  for y,x in Q:
   if H>y>-1<x<W>0<(c:=g[y][x]):C+=c<3;g[y][x]=0;Q+=(y,x-1),(y-1,x),(y+1,x),(y,x+1)
  a+=C>4
 return[[a*8]]