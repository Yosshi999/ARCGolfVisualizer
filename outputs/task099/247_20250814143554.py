def p(g):
 for i in range(9):
  for j in range(9):
   if g[i][j]==g[i+1][j]==g[i][j+1]==1:
    H=0
    while i+H<10and g[i+H][j]==1:H+=1
    c=g[i+(H-1)//2][j+2]
    for I in range(i-1,i+H):
     for J in range(j,j+5):g[I][J]=g[I][J]or c
 return g