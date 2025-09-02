def p(g):
 k=sum(g,[]).count(0);h=[[0]*k*3for _ in g*k]
 for i in range(9-k):
  for j in 0,1,2:h[i//k*3+j][i%k*3:i%k*3+3]=g[j]
 return h