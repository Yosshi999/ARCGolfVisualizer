f=lambda g:[x for x,y in zip(g,[0]+g)if x!=y]
p=lambda g:[*map(list,zip(*f([*zip(*f([[*filter(int,v)]for v in g if max(v)]))])))]