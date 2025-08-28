r=range(16)
p=lambda g:[[(g[i][j]-4|g[~i][~j]-4)+4for j in r]for i in r]