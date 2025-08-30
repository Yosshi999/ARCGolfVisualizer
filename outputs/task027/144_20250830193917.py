r=range(10)
f=lambda g,b:[[g[i][j]or 2*g[-i-b][-j-b]for j in r]for i in r]
s=lambda g:sum(sum(g,[]))
p=lambda g:(C:=f(g,0),D:=f(g,1))[s(C)>s(D)]