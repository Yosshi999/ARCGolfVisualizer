def p(g):
 h=[v*2for v in g*2]
 for i in range(len(h)):
  for j in range(len(h[0])):
   if h[i][j]%8:
    if i>0:
     if j>0and h[i-1][j-1]%8<1:
      h[i-1][j-1]=8
     if j<len(h[0])-1and h[i-1][j+1]%8<1:
      h[i-1][j+1]=8
    if i<len(h)-1:
     if j>0and h[i+1][j-1]%8<1:
      h[i+1][j-1]=8
     if j<len(h[0])-1and h[i+1][j+1]%8<1:
      h[i+1][j+1]=8
 return h