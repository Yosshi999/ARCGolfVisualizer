def p(g):
 h=[*map(list,g)]
 for k in range(81):
  if g[i:=k//9][j:=k%9]:h[i-1][s:=slice(j-1,j+2)]=h[i+1][s]=[5,1,5];h[i][s]=[1,0,1]
 return h