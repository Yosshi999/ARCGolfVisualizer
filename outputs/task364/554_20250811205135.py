def p(g):
 Q=lambda g,i,j,c:(i>0and g[i-1][j]==c)+2*(j>0and g[i][j-1]==c)+4*(i<len(g)-1and g[i+1][j]==c)+8*(j<len(g[0])-1and g[i][j+1]==c)
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==3:
    q=Q(g,i,j,3)
    if q in{3,6,12,9}:g[i][j]=1
    if q in{7,14,13,11}:g[i][j]=2
 for _ in range(900):
  for i in range(len(g)):
   for j in range(len(g[0])):
    if g[i][j]==3:
     q=Q(g,i,j,1)
     if q in{5,10}:g[i][j]=6
     elif q:g[i][j]=1
    if g[i][j]>0and Q(g,i,j,2):g[i][j]=2
    if 2!=g[i][j]>0and Q(g,i,j,6):g[i][j]=6
 return g