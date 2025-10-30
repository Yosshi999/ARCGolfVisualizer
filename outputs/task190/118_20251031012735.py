r=range(10)
p=lambda g:[g:=[[g[~j][i]|g[-j][i-1]*(g[1-j][i-2]>g[-j][i-2]<i>1<j)for j in r]for i in r]for _ in g*2][19]