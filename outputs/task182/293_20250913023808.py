def T(g,H):
 for k in range(256):
  if all((H[I:=K//5][J:=K%5]>0)==g[(i:=k//16)+I][(j:=k%16)+J]for K in range(25)):
   for d in range(5):g[i+d][j:j+5]=H[d]
def p(g):
 for i in range(14):
  for j in range(14):
   if{*g[i][j:j+7]+g[i+6][j:j+7]}=={5}:T(g,[v[j+1:j+6]for v in g[i+1:i+6]]);return g