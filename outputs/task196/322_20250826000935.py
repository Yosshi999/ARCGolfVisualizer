def p(g):
 H=len(g);W=len(g[0])
 for i in range(H):
  for j in range(W):
   if g[i][j]==1:
    w=h=0
    while j+w<W and g[i][j+w]:w+=1
    while i+h<H and g[i+h][j]:h+=1
    if w>2and h>2and sum(v for u in g[i:i+h]for v in u[j:j+w])==w*2+h*2-4:
     for I in range(i,i+h):
      for J in range(j,j+w):g[I][J]*=3
 return g