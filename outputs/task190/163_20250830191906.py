def p(g,t=96):
 for k in range(64):
  if(c:=g[(i:=k//8)+1][(j:=k%8)+1])*(g[i][j:j+2]==[c,0])*i*j:g[i-1][j-1]=c
 return p([*map(list,zip(*g[::-1]))],t-1)if t else g