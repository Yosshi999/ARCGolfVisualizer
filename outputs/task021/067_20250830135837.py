f=lambda g:[x for*x,in zip(*g)if g!=(g:=x)][::2]
p=lambda g:f(f(g))