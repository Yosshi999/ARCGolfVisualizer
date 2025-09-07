r=range(7)
p=lambda g,d=4:p([*zip(*[[g[i][j]or(i*j>0)*g[i][j-1]*g[i-1][j]>9for j in r]for i in r])][::-1],d-1)if d else g