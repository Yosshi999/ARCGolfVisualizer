f=lambda g:[*map(list,zip(*[x for x,y in zip(g,[0]+g)if x!=y]))]
p=lambda g:f(f(g))