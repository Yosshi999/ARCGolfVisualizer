R=range(6)
V=[1,1,0,0,1,1,-1,-1]
p=lambda g:[[[g[y][x]|g[Y-V[y-Y]][X-V[x-X]]for x in R]for y in R]for Y in R for X in R if g[Y][X]][0]