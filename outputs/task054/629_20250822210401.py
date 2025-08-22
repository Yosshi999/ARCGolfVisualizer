def p(g):
 B=g[0][0];f=sum(g,[]);C=max({*f}-{B},key=f.count)
 H=[(i+1,j+1)for i in range(28)for j in range(28)if g[i+1][j+1]not in[B,C]and g[i][j+1]==C]
 V,I,J=max((sum([C!=g[i+u][j+v]!=B for u in range(-2,3)for v in range(-2,3)if abs(u)+abs(v)<=2]),i,j)for i in range(2,28)for j in range(2,28)if{g[i][j]}-{B,C})
 for i,j in H:
  for u in [-1,0,1]:
   for v in [-1,0,1]:
    if g[I+u][J+v]!=B:g[i+u][j+v]=g[I+u][J+v]
  for u,v,x,y,U,V in[(i-2,j,-1,0,I-2,J),(i+2,j,1,0,I+2,J),(i,j-2,0,-1,I,J-2),(i,j+2,0,1,I,J+2)]:
   while g[u][v]!=B and g[U][V]!=B:g[u][v]=g[U][V];u+=x;v+=y
 for u in range(I-2,I+3):g[u][J-2:J+3]=[B]*5
 return g