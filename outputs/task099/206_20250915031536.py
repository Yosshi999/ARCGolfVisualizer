def p(g):
 for i in range(9):
  for j in range(9):
   if g[i][j-1:j+2]==[1,0,1]:
    c=max(g[i+1]+g[i+2]);i-=1
    while g[i].count(1)<5:
     for k in range(j-2,j+3):g[i][k]=g[i][k]or c
     i+=1
 return g