r=range(9)
p=lambda g:[[g[i][j]or any(sum(v[j-(j>0):j+2])for v in g[i-(i>0):i+2])for j in r]for i in r]