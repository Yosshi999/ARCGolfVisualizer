r=range(11)
p=lambda g:[[5*(g[i][j]==5)or all((f:=lambda i,j:sum(sum(v[j:j+3])for v in g[i&~3:][:3]))(i,j&~3)>=f(z,z%4*4)for z in r)*sum({*sum(g,[-5])})for j in r]for i in r]