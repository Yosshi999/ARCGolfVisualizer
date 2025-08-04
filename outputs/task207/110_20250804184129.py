def p(g):
 h=[]
 for i in[0,3]:
  for j in[0,3]:
   h+=[g[i][j:j+2],g[i+1][j:j+2]],
 return min(h,key=h.count)