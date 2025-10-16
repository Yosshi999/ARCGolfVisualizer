R=range(6)
p=lambda g:[[[g[y][x]or g[Y+1+14%((y-Y-12)//2)][X+1+14%((x-X-12)//2)]for x in R]for y in R]for Y in R for X in R if g[Y][X]][0]