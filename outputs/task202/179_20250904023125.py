f=lambda g:[[x-x*(x in[y for x,y in zip(v,[max(v)for v in zip(*g)])if x<1])for x in v]for v in g]
R=lambda g:[*zip(*g)]
p=lambda g:any(len({*v})<2 for v in g)and R(f(R(g)))or f(g)