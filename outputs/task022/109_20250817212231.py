r=range(11);d=[-1,0,1]
p=lambda g:[[max(g[i+x][j+y]for i in r for j in r if g[i][j]==5)for y in d]for x in d]