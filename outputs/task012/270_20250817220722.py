r=range(12)
def p(g):
 h=sum(g,[])
 c=min(h,key=h.count)
 d=sum({*h})-c
 G=[*map(list,g)]
 for i in r:
  for j in r:
   if G[i][j]==c:
    g[i-2][j-2:j+3]=g[i+2][j-2:j+3]=[c,0,d,0,c]
    g[i-1][j-2:j+3]=g[i+1][j-2:j+3]=[0,c,d,c,0]
    g[i][j-2:j+3]=[d,d,c,d,d]
 return g