def p(g):
 Z={c:([0]*16,[0]*16)for c in range(10)}
 for i,v in enumerate(g):
  for j,c in enumerate(v):
   Z[c][0][i]+=1;Z[c][1][j]+=1
 del Z[0]
 for c,(I,J) in Z.items():
  if len(set(I))==len(set(J))==2:F=c
  elif len(set(I))>1:B=c
 I=[i for i in range(16)if Z[B][0][i]>0and Z[F][0][i]<1][0]
 J=[j for j,c in enumerate(g[I]) if c>0]
 assert len(J)>0
 J=(J[(len(J)-1)//2]+J[len(J)//2])/2
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==F:g[i][j]=g[i][int(J+J-j)]
 return g