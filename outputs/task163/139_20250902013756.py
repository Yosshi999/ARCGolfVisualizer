R=range(11)
p=lambda g:[[5+(g[y][x]-5and sum((g[Y+y//4][X+x//4]==4)*g[Y+y%4][X+x%4]for Y in[0,4,8]for X in[0,4,8])-5)for x in R]for y in R]