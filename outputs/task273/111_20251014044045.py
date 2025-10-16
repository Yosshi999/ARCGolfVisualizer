r=range(10)
p=lambda g:[[g[i][j]+(4==sum(sum(u[:j])+u[j]/4for u in g[:i])%16>max(g[i]))*2for j in r]for i in r]