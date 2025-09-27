r=range(9)
p=lambda g:[g:=[[g[~j][i]or(g[-j][i]==1)*7+4*(g[-j][i-1]==2)for j in r]for i in r]for _ in g][3]