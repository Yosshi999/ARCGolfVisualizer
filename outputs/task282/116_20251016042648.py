R=range(9)
p=lambda g:[[(0,1,5,0)[min(3,*((Y-y)**2+(X-x)**2for Y in R for X in R if g[Y][X]))]for x in R]for y in R]