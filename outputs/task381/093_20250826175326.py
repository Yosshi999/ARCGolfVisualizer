r=range(10)
p=lambda g:[[(v:=g[i])[j]or(2in{*v[:j]}&{*v[j:]})*(0<i<9)*9for j in r]for i in r]