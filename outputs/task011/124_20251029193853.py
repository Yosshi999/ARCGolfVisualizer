r=range(11)
p=lambda g,k=0:8in sum(s:=[[5*(g[i][j]==5)or g[i//4+k//3*4][j//4+k%3*4]for j in r]for i in r],g)and p(g,k+1)or s