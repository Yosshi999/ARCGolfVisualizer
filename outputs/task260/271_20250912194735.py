r=range(10)
def p(g):
 C=sum({*sum(g,[-5])})
 def f(k,c):
  q=0
  for i in r:
   j=i+k
   if 0<=j<10:q+=g[i][j]==5;g[i][j]=c
  return q
 L=[f(k,0)for k in range(-11,12)]
 for k in range(-9,10):
  if L[k+11]==0 and (L[k+10]+L[k+12]>1 or L[k+9]+L[k+13]==1):f(k,C)
 return g