r=range(6)
p=lambda g:[[g[i+3*(a:=g[6][0]//4)-6][j+3*(b:=g[0][6]//4)-6]/3*g[i//3-a][j//3-b]for j in r]for i in r]