r=range(11)
p=lambda g:[[5*(g[i][j]==5)or max((g[(x:=z&12)+i//4][z%3*4+j//4]==4)*g[x+i%4][z%3*4+j%4]for z in r)for j in r]for i in r]