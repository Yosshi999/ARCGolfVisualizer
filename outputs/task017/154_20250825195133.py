r=range(21)
p=lambda g:[[[max([*map(max,*g[i%d::d])][j%d::d])for j in r]for i in r]for d in r[5:10]if len({*sum([v[1::d]for v in g[2::d]],[])}-{0})==1][0]