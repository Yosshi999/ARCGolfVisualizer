r=range(4)
p=lambda g:[[max(g[i][j::5]+g[i+5][j::5],key=bool)for j in r]for i in r]