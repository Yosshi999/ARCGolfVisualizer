def T(g,H):
 for i in range(16):
  for j in range(16):
   if all((g[i+I][j+J]>0)==(H[I][J]>0)for I in range(5) for J in range(5)):
    for I in range(5):g[i+I][j:j+5]=H[I]
def p(g):
 for i in range(14):
  for j in range(14):
   if set(g[i][j:j+7]+g[i+6][j:j+7]+[v[j]for v in g[i:i+7]]+[v[j+6]for v in g[i:i+7]])=={5}:T(g,[v[j+1:j+6]for v in g[i+1:i+6]]);return g