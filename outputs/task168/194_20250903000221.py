def p(g):
 for _ in[0]*4:
  for i in range(9):
   for j in range(9):
    c=g[i][j+1]
    if min(g[i+1][j:j+2])==c>0:exec('i-=1;j-=1;g[i][j]=c;'*min(i,j))
  g=[*map(list,zip(*g[::-1]))]
 return g