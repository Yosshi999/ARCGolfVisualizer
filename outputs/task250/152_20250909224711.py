R=range(10)
p=lambda g,d=4:d and p([*zip(*[[g[y],[*map(max,*g[:(Y:=min(y for y in R if 2 in g[y]))])],[0]*10][(y<Y)+(y<Y-1)]for y in R][::-1])],d-1)or g