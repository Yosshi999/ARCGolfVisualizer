r=range(19)
p=lambda g:[g:=[[g[j][i]|g[j][~i+2*(j+2<i<16-j)]for j in r]for i in r]for _ in r][-1]