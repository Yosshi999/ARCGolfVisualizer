r=range(10)
p=lambda g:[[2if sum(v[:j].count(4)for v in g[:i])%4==1 and 4not in g[i]and 4not in[*zip(*g)][j]else g[i][j]for j in r]for i in r]