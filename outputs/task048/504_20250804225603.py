def R(g):
 for i in range(len(g)-1):
  for j in range(len(g[0])-1):
   if g[i][j]==g[i+1][j]==g[i][j+1]==g[i+1][j+1]==2:
    g[i][j]=g[i+1][j]=g[i][j+1]=g[i+1][j+1]=3
    return
def Q(g,c):
 for _ in range(900):
  for i in range(len(g)):
   for j in range(len(g[0])):
    if i>0 and g[i-1][j]==2 or i<len(g)-1 and g[i+1][j]==2 or j>0 and g[i][j-1]==2 or j<len(g[0])-1 and g[i][j+1]==2:
     if g[i][j]==c:g[i][j]=2
     if g[i][j]==3:return True
def p(g):
 R(g)
 if Q(g,8):return [[8]]
 else:return [[0]]