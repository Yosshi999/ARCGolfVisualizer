f=lambda g:[[x-x*(x in[y for x,y in zip(v,[max(v)for v in zip(*g)])if x<1])for x in v]for v in g]
p=lambda g:any(len({*v})<2for v in g)and[*zip(*f([*zip(*g)]))]or f(g)