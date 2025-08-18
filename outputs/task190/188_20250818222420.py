def p(g):
 for _ in[0]*4:
  for k in range(64):
   if g[i:=k//8][j:=k%8]*min(g[i+1][j+1:j+3]):
    d=0;exec('g[i-d][j-d]=g[i][j];d+=1;'*-~min(i,j))
  g=[*map(list,zip(*g[::-1]))]
 return g