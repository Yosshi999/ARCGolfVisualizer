r=range(11)
p=lambda g:[[5*(g[i][j]==5)or sum((g[x+i//4][y+j//4]==4)*g[x+i%4][y+j%4]for x in[0,4,8]for y in[0,4,8])for j in r]for i in r]