def p(g):
 s=sum(g,[])
 k=s.count(0)
 h=[[0]*k*3for _ in[0]*3*k]
 c=max(s)
 n=s.count(c)
 for i in range(n):
  for j in[0,1,2]:h[i//k*3+j][i%k*3:i%k*3+3]=g[j][:3]
 return h