r=range(16)
def p(g):
 I=J=K=L=0
 for i in r:
  for j in r:
   for k in r:
    for l in r:
     if (i+k<17)*(j+l<17)*(g[i][j]>0)*(K*L<k*l) and 1==len(set(sum([v[j:j+l]for v in g[i:i+k]],[]))):I=i;J=j;K=k;L=l
 return[[g[i][j]*(I<=i<I+K)*(J<=j<J+L)for j in r]for i in r]