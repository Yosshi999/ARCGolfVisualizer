def p(g):
 h,w=len(g),len(g[0])
 count=0
 for r in range(h-1):
  for c in range(w-1):
   if (g[r][c]==1 and g[r+1][c]==1 and 
       g[r][c+1]==1 and g[r+1][c+1]==1):
    count+=1
 o=[[0]*5 for _ in range(1)]
 for i in range(min(count,5)):
  o[0][i]=1
 return o