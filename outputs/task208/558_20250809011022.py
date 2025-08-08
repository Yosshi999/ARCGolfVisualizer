def T(g,C,H,W):
 for i in range(1,21-H):
  for j in range(1,21-W):
   if all(v==0 for u in g[i:i+H] for v in u[j:j+W]):
    for J in range(j-1,j+W+1):g[i-1][J]=g[i+H][J]=C
    for I in range(i-1,i+H+1):g[I][j-1]=g[I][j+W]=C
def p(g):
 for c in range(1,10):
  for i in range(21):
   for j in range(21):
    for k in range(i+3,21):
     for l in range(j+3,21):
      if all(v==0for u in g[i+1:k]for v in u[j+1:l]) and len(set(g[i][j:l+1]+g[k][j:l+1]+[r[j] for r in g[i+1:k]]+[r[l] for r in g[i+1:k]]))==1 and g[i][j]>0:
       T(g,g[i][j],k-i-1,l-j-1);return g