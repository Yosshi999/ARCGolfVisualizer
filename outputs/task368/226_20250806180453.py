r=range(10)
def p(g):
 I,J=zip(*[(i,j)for i in r for j in r if g[i][j]%5]);l=max(J)-min(J)+1
 for i in r:
  for j in r:
   if g[i][j]==5:
    for x in range(max(I)-min(I)+1):g[i+x][j:j+l]=g[min(I)+x][min(J):min(J)+l]
 return g