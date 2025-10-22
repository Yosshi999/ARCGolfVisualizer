r=0,1,2,3
p=lambda g:[[max(g[i][j::5])or max(g[i+5][j::5])for j in r]for i in r]