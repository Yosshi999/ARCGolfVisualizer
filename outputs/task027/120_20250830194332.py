r=range(10)
p=lambda g:min([[[g[i][j]or 2*g[-i-b][-j-b]for j in r]for i in r]for b in[0,1]],key=lambda x:sum(sum(x,[])))