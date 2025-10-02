r=range(10)
p=lambda g:[g:=[[((c:=g[j][i])!=d)*(c|sum({*sum(g,[-5])})*any(j-i==y-x for y in r for x in r if[0,5,0,0]==g[y-1][x:x+2]+g[y][x:x+2]))for j in r]for i in r]for d in[g,5]][1]