r=range(10)
p=lambda g:[g:=[[g[~i][j]|8*(i>n<g[~i+n][j-2*n]*g[~i+2*n][j-n]%2*j)for i in r]for j in r]for n in[g.count(max(g))]*4][3]