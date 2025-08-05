r=range(17)
p=lambda g:[[(g[i][j],g[5][0])[g[i][j]<g[i%6][j%6]]for j in r]for i in r]