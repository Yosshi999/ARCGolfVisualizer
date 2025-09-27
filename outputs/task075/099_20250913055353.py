r=range
p=lambda g:[[(g[y%3][X:=~-x%3]*g[y-y%3+1][x-X+1],g[y][x])[x<4]for x in r(13)]for y in r(9)]