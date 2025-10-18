r=range(6)
p=lambda g:[[g[i+all(g[2])*3][j+g[0][2]//8*3]/3*g[i//3-g[6][0]//4][j//3-g[0][6]//4]for j in r]for i in r]