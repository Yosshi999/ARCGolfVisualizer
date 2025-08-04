def p(g):
 h=[];r=[0,3]
 for i in r:
  for j in r:h+=[g[i][j:j+2],g[i+1][j:j+2]],
 return min(h,key=h.count)