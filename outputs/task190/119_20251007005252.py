r=range(10)
p=lambda g:[g:=[[g[j][~i]|g[j-1][-i]*(g[j-2][1-i]>g[j-1][1-i]<i>1<j)for j in r]for i in r]for _ in g*2][19]