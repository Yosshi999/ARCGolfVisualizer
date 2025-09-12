def p(g):
 def f(k,c,q=0):
  for i in range(10):
   if 0<=(j:=i+k)<10:q+=g[i][j]==5;g[i][j]=c
  return q
 C=sum({*sum(g,[-5])});L=[f(k-11,0)for k in range(23)];[f(k-9,C)for k in range(19)if(L[k+1]+L[k+3]>1)|(L[k]+L[k+4]==1)>L[k+2]];return g