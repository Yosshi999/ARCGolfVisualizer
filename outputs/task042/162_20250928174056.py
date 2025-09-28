r=range(10)
p=lambda g:[g:=[[g[~i][j]|8*(i>=2*(n:=sum(g,[]).count(3)//8+1)<=j>=g[~i+n][j-n]<g[~i+n][j-2*n]==3==g[~i+2*n][j-n])for i in r]for j in r]for _ in g][3]