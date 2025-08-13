r=range(4)
p=lambda g:[[g[i][j]or g[i][j+5]or g[i+5][j]or g[i+5][j+5]for j in r]for i in r]