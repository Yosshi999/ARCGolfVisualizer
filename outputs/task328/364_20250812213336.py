def p(g):
 I=[];J=[];C=[]
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    C+=[g[i][j]];I+=[i];J+=[j]
 for i in range(len(g)):
  for j in range(len(g[0])):
   M=[max(abs(i-u),abs(j-v))for u,v in zip(I,J)]
   m=[abs(i-u)+abs(j-v)for u,v in zip(I,J)]
   k=m.index(min(m))
   if sum(c==m[k] for c in m)==1and M[k]%2==0:g[i][j]=C[k]
 return g