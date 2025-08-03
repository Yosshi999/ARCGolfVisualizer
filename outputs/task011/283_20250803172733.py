def p(g):
 h=[list(v)for v in g]
 for i in range(3):
  for j in range(3):
   if len({v for u in g[i*4:i*4+3]for v in u[j*4:j*4+3]})==5:
    for I in range(3):
     for J in range(3):
      for k in range(3):
       for l in range(3):
        h[I*4+k][J*4+l]=g[i*4+I][j*4+J]
 return h