r=[0,3]
def p(g):
 h=[]
 for i in r:
  for j in r:h+=[g[i][j:j+2],g[i+1][j:j+2]],
 return min(h,key=h.count)