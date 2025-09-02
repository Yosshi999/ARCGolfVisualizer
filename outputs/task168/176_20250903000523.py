def p(g):
 for _ in[0]*4:
  for k in range(81):i=k//9;j=k%9;c=g[i][j+1];exec('i-=1;j-=1;g[i][j]=c;'*min(i,j)*(min(g[i+1][j:j+2])==c>0))
  g=[*map(list,zip(*g[::-1]))]
 return g