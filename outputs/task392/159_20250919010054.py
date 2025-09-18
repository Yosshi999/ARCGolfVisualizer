r=range(10)
p=lambda g:[[(c:=max(sum(g,[])),5,5)[min(max(i-x,x-i,j-y,y-j)for x in r for y in r if g[x][y])%(3-(f'{c}, 0, {c}'in str(g)))]for j in r]for i in r]