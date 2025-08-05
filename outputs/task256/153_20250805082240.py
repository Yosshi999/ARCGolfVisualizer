def p(g):
 for i,v in enumerate(g):
  if(s:=sum(v)//2):
   for j in range(9):
    k=s+i-j
    if j<i:g[j][:k]=[3]*k
    if j<s:g[k][:j]=[1]*j
   return g