r=range(9)
p=lambda g:[[g[i//3*3+1][j//3*3+1]&1for j in r]for i in r]