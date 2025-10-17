R=range(6)
V=1,0,1,-1
p=lambda g:[[[g[y][x]|g[Y-V[y-Y>>1]][X-V[x-X>>1]]for x in R]for y in R]for Y in R for X in R if g[Y][X]][0]