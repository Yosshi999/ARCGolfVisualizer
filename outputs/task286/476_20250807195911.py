def p(g):
 s=set()
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j] not in [0,8]:s.add(g[i][j])
 s,t=list(s)
 for _ in range(900):
  for i in range(len(g)):
   for j in range(len(g[0])):
    if g[i][j]==0:
     if i>0and s==g[i-1][j]or j>0and s==g[i][j-1]or i<len(g)-1and s==g[i+1][j]or j<len(g[0])-1and s==g[i][j+1]:g[i][j]=t
     if i>0and t==g[i-1][j]or j>0and t==g[i][j-1]or i<len(g)-1and t==g[i+1][j]or j<len(g[0])-1and t==g[i][j+1]:g[i][j]=s
 return g