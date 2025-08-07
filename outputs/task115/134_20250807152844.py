f=lambda g:[[w]for j,w in enumerate(g[0])if g[0][j-1]!=w]
t=lambda g:[*map(list,zip(*g))]
p=lambda g:(t(f(g)),f(t(g)))[len({*g[0]})<2]