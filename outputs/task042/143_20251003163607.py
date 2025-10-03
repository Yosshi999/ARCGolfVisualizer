r=range(10)
p=lambda g:[g:=[[g[~i][j]|8*(i>(n:=sum(g,g).count(3)//8+1)<j>0<g[~i+n][j-2*n]&g[~i+2*n][j-n]<4)for i in r]for j in r]for _ in g][3]