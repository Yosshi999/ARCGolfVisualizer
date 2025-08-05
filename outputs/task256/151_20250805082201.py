def p(g):
 for i,v in enumerate(g):
  if(s:=sum(v)//2):
   for j in range(i):k=s+i-j;g[j][:k]=[3]*k
   for j in range(s):g[i+s-j][:j]=[1]*j
   return g