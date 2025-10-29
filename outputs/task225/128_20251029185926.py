R=range(6)
V=1,0,1,-1
p=lambda g,Z=0:g[Y:=Z//6][X:=Z%6]and[[g[y][x]|g[Y-V[y-Y>>1]][X-V[x-X>>1]]for x in R]for y in R]or p(g,Z+1)