r=range(7)
p=lambda g,d=4:p([[g[j][i]or(i*j>0)*g[j][i-1]*g[j-1][i]>9for j in r]for i in r][::-1],d-1)if d else g