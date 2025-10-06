r=range(12)
def p(g,b=0):
 for i in r:
  for j in r:
   if g[i][j]:
    if all(g[i-1][b+1:j]):l=j+~b;g[i][b+1:j]=[5+l]*l
    b=j
 return g