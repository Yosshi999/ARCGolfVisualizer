def p(g):
 a={i:[] for i in range(10)}
 A=[[]for _ in range(10)]
 for i in range(len(g)-1):
  for j in range(len(g[0])-1):
   if g[i][j]==g[i+1][j]==g[i][j+1]and g[i][j]!=g[i+1][j+1]:
    a[g[i][j]].append((i+1,j+1));A[g[i][j]].append(1)
   if g[i][j]==g[i][j+1]==g[i+1][j+1]and g[i][j]!=g[i+1][j]:
    a[g[i][j]].append((i,j));A[g[i][j]].append(2)
   if g[i][j]==g[i+1][j]==g[i+1][j+1]and g[i][j]!=g[i][j+1]:
    a[g[i][j]].append((i,j));A[g[i][j]].append(3)
   if g[i+1][j]==g[i+1][j+1]==g[i][j+1]and g[i+1][j]!=g[i][j]:
    a[g[i+1][j]].append((i+1,j+1));A[g[i+1][j]].append(4)
 b=a[9-A[::-1].index([1,2,3,4])]
 return [v[b[0][1]:b[3][1]]for v in g[b[0][0]:b[3][0]]]