r=range(6)
p=lambda g:[[sum(g[i-k][j-k]for k in r if 0<=i-k<3 and 0<=j-k<3)for j in r]for i in r]