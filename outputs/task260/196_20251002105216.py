r=range(10)
p=lambda g:[g:=[[((c:=g[j][i])*d!=5)*(c|(sum({*sum(g,[-5])})*any(j-i==y-x+1for y in r[:9]for x in r[:9]if g[y][x:x+2]+g[y+1][x:x+2]==[0,5,0,0])))for j in r]for i in r]for d in[0,1]][1]