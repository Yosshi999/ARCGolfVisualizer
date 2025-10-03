r=range(12)
p=lambda g:[g:=[[g[j][~i]or(g[j-1][-i]*g[j-2][1-i]>4>0<i>1<j)*3for j in r]for i in r]for _ in g*4][39]