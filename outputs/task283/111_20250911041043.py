R=range(10)
p=lambda g:[[g[i][j]and(1<<sum(sum(v[j-(j>0):j+2])for v in g[i-(i>0):i+2])%4)for j in R]for i in R]