r=range(9)
p=lambda g:[[sum({*sum(g,[-2])})*(g[i][j]+min((I:=abs(i-x),J:=abs(j-y),-2<I-J<g[x][y]==2)for x in r for y in r if g[x][y])[2]>0)for j in r]for i in r]