def p(g):
 return[[(g[i][j],g[5][0])[g[i][j]<g[i%6][j%6]]for j in range(17)]for i in range(17)]