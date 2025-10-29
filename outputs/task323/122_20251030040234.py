r=range(13)
p=lambda g:[[g[i][j]or(d:=g.index(v:=max(g))-i)and(abs(j-v.index(8)+~d+2*(d>0))<=~d%2)*5for j in r]for i in r]