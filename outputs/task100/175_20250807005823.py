r=range(10)
def p(g):
 x=[]
 for c in{*sum(g,[])}-{0}:I,J=zip(*[(i,j)for i in r for j in r if g[i][j]==c]);x+=((max(I)-min(I)+1)*(max(J)-min(J)+1),c),
 return[[max(x)[1]]*2]*2