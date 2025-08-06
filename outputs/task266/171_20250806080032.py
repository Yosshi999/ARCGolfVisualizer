def p(g):
 g=[v+[0]for v in g*2]
 for k in range(15):
  if g[i:=k//5][j:=k%5]:g[i][j]=0;g[i-1][j-1]=3;g[i-1][j+1]=6;g[i+1][j-1]=8;g[i+1][j+1]=7;return[v[:5]for v in g[:3]]