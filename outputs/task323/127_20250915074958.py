r=range(13)
p=lambda g:[[(d:=g.index(v:=max(g))-i)and(d%2<=(j-v.index(8)-d)*(1|-(d>0))<3-d%2)*5or g[i][j]for j in r]for i in r]