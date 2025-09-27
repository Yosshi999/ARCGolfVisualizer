r=range(7)
p=lambda g:[g:=[[g[j][i]or i*j>0<9<g[j][i-1]*g[j-1][i]for j in r]for i in r][::-1]for _ in g][3]