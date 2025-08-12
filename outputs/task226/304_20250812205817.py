def p(g):
 h=zip(*g)
 I=[0];J=[0]
 for i,v in enumerate(g):
  if sum(v)==50:I+=[i+1]
 for j,v in enumerate(h):
  if sum(v)==50:J+=[j+1]
 I+=[11];J+=[11]
 M=1+(len(I)>4);N=1+(len(J)>4)
 for m in range(3):
  for i in range(I[M*m],I[M*m+1]-1):
   for j in range(J[N*m],J[N*m+1]-1):
    g[i][j]=m+1
 return g