def p(g):
 x=[[]for _ in range(10)]
 for i in range(10):
  for j in range(10):
   x[g[i][j]].append((i,j))
 c=list(map(len,x)).index(1)
 I,J=x[c][0]
 h=[[0]*10for i in range(10)]
 for i in range(I-1,I+2):
  for j in range(J-1,J+2):
   h[i][j]=2
 h[I][J]=c
 return h