R=range(12)
p=lambda g,d=48:d and p([[g[y][x]or(sum(v:=[g[y-1][x-1],g[y-2][x-2]])>4>all(v)>0<x>1<y)*3for y in R]for x in R][::-1],d-1)or g