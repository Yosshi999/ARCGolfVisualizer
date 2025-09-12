def p(g):
 f=lambda i,j:sum(sum(v[j:j+3])for v in g[i:i+3])
 return[[5*(g[i][j]==5)or(f(i&~3,j&~3)==max(f(x,y)for x in[0,4,8]for y in[0,4,8]))*sum({*sum(g,[-5])})for j in range(11)]for i in range(11)]