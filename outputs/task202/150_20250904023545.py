f=lambda g:[[x-x*((0,x)in zip(v,[max(v)for v in zip(*g)]))for x in v]for v in g]
p=lambda g:any(len({*v})<2for v in g)and[*zip(*f([*zip(*g)]))]or f(g)