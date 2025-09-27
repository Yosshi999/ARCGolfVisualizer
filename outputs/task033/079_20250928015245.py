r=range(17)
p=lambda g:[[g[i][j]or(0<g[i%6][j%6])*g[5][5]for j in r]for i in r]