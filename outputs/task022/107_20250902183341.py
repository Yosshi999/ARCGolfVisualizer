d=[-1,0,1]
p=lambda g:[[max(g[i+x][j+y]for k in range(121)if g[i:=k//11][j:=k%11]==5)for y in d]for x in d]