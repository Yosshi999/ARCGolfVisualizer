f=lambda g:[[a]for a,b in zip(g[0],[0]+g[0])if a!=b]
t=lambda g:[*map(list,zip(*g))]
p=lambda g:(t(f(g)),f(t(g)))[len({*g[0]})<2]