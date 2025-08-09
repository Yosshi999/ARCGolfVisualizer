def p(g):
 for k in [2,3,4]:
  if all(v==0for u in g[:k]for v in u[:k]):K=k
 H=[];C=g[0][K];m=n=30;M=N=0
 for i in range(K,len(g)-K-1,K+1):
  h=[]
  for j in range(K,len(g[0])-K-1,K+1):
   if g[i][j]!=C and g[i][j]==g[i+K+1][j]==g[i][j+K+1]==g[i+K+1][j+K+1]:
    h+=[g[i][j]];m=min(m,i//(K+1));n=min(n,j//(K+1));M=max(M,i//(K+1));N=max(N,j//(K+1))
   else:h+=[0]
  H+=[h]
 return [u[n:N+1]for u in H[m:M+1]]