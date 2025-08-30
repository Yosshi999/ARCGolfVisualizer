def p(g,t=4):
 for k in range(64):
  if(c:=g[i:=k//8][j:=k%8])*min(g[i+1][j+1:j+3]):d=0;exec('g[i-d][j-d]=c;d+=1;'*-~min(i,j))
 return p([*map(list,zip(*g[::-1]))],t-1)if t else g