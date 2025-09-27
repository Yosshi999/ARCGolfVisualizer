r=range(10)
p=lambda g:min((sum(sum(x:=[[g[i][j]or 2*g[-i-b][-j-b]for j in r]for i in r],[])),x)for b in[0,1])[1]