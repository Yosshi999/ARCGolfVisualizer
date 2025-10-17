r=range(19)
p=lambda g:[g:=[[g[j][i]|g[j][~i+2*(j<i-2<8)]for j in r]for i in r]for _ in r][-1]