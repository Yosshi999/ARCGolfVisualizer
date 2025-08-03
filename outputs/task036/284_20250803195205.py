def p(g):
 a=[];b=[]
 for c in range(10):
  A,B,C,D=30,-1,30,-1
  for i in range(30):
   for j in range(30):
    if g[i][j]==c:
     A=min(A,i);B=max(B,i);C=min(C,j);D=max(D,j)
  a.append((A,B,C,D));b.append((A-B)*(C-D))
 A,B,C,D=a[b.index(min(b))]
 return [v[C:D+1]for v in g[A:B+1]]