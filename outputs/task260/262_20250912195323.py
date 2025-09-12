def p(g):
 def f(k,c,q=0):
  for i in range(10):
   if 0<=(j:=i+k)<10:q+=g[i][j]==5;g[i][j]=c
  return q
 C=sum({*sum(g,[-5])});L=[f(k,0)for k in range(-11,12)]
 for k in range(-9,10):
  if L[k+11]==0 and (L[k+10]+L[k+12]>1 or L[k+9]+L[k+13]==1):f(k,C)
 return g