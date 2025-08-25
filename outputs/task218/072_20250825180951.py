f=lambda g:[x for*x,in zip(*g)if g!=(g:=x)and any(x)]
p=lambda g:f(f(g))