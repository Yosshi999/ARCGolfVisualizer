r=range(11)
p=lambda g:[[5*(g[i][j]==5)or all((f:=lambda i,j:sum(sum(v[j:j+3])for v in g[i:i+3]))(i&~3,j&~3)>=f(x,y)for x in[0,4,8]for y in[0,4,8])*sum({*sum(g,[-5])})for j in r]for i in r]