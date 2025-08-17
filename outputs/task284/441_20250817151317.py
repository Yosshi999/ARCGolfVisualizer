def f(g):
 g=[*map(list,zip(*g))]
 for i,v in enumerate(g):
  if len(set(v))==3:
   a,b=[*set(v)-{0}];m,M=v.index(a),v.index(b);m,M=min(m,M),max(m,M);c=(m+M)//2;a,b=g[i][m],g[i][M]
   for j in range(m,c):g[i][j]=a
   for j in range(c+2,M+1):g[i][j]=b
   g[i-1][c-1]=g[i-2][c-1]=g[i+1][c-1]=g[i+2][c-1]=g[i-2][c]=g[i+2][c]=a
   g[i-1][c+2]=g[i-2][c+2]=g[i+1][c+2]=g[i+2][c+2]=g[i-2][c+1]=g[i+2][c+1]=b
   return g
 return g
p=lambda g:f(f(g))