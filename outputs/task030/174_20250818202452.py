def p(g):
 e=enumerate;o=[[0]*len(v)for v in g];f=lambda c:[(i,j)for i,v in e(g)for j,x in e(v)if x==c]
 for k in 1,2,4:
  for p,q in zip(f(1),f(k)):o[p[0]][q[1]]=k
 return o