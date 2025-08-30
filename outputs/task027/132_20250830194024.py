r=range(10)
f=lambda g,b:[[g[i][j]or 2*g[-i-b][-j-b]for j in r]for i in r]
p=lambda g:min(f(g,0),f(g,1),key=lambda x:sum(sum(x,[])))