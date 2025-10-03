r=range(11)
p=lambda g:[[5*(g[i][j]==5)or max((g[z//4*4+i//4][z%3*4+j//4]==4)*g[z//4*4+i%4][z%3*4+j%4]for z in r)for j in r]for i in r]