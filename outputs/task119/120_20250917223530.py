r=range(12)
p=lambda g:[g:=[[g[j][i]or(g[j-1][i-1]*g[j-2][i-2]>4>0<i>1<j)*3for j in r]for i in r][::-1]for _ in g*4][39]