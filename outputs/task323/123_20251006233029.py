r=range(13)
p=lambda g:[[(d:=g.index(v:=max(g))-i)and(abs(j-v.index(8)+~d+2*(d>0))<=~d%2)*5or g[i][j]for j in r]for i in r]