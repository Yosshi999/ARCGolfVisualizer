def f(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==2:
    W=0
    while j+W<len(g[0])and g[i][j+W]==2:W+=1
    h=[r[j:j+W]for r in g[i:i+W]];return W,h
def p(g):
 W,h=f(g)
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if all([any(0!=x!=2for x in v[j:j+3])for v in g[i:i+3]])and all([any(0!=x!=2for x in v[i:i+3])for v in [*zip(*g)][j:j+3]]):
    s=W//3
    for I in range(3):
     for J in range(3):
      for u in range(s):
       for v in range(s):
        h[1+s*I+u][1+s*J+v]=g[i+I][j+J]
    return h