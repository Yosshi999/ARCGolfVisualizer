R=range(10)
p=lambda g,d=4:d and p([[g[y][x]|max(g[Y:=y-k][X:=x-k]*(0<Y>0<X*g[Y+1][X]*g[Y][X+1])for k in R[2:])for y in R]for x in R][::-1],d-1)or g