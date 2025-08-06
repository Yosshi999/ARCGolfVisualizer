r=range(100);m=min;M=max
def p(g):
 I,J=zip(*[(i,j)for k in r if g[i:=k//10][j:=k%10]%5]);l=M(J)-m(J)+1
 for k in r:
  if g[i:=k//10][j:=k%10]==5:
   for x in range(M(I)-m(I)+1):g[i+x][j:j+l]=g[m(I)+x][m(J):m(J)+l]
 return g