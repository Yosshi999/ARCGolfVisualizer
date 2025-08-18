def p(g):
 n=len(g);i=j=d=0;L=[(0,1),(1,0),(0,-1),(-1,0)]
 for _ in[0]*n*n:
  k,l=L[d];g[i][j]=3;x=i+k;y=j+l;X=x+k;Y=y+l
  if(x<0)+(x>=n)+(y<0)+(y>=n)+((0<=X<n)*(0<=Y<n)and g[X][Y]):d=(d+1)%4
  else:i=x;j=y
 return g