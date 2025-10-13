r=range(10)
p=lambda g:[g:=[[g[~i][~j]|(i>0<j)*g[-i][-j]&c&g[1-i][1-j]for j in r]for i in r]for c in[1,2]*8][15]