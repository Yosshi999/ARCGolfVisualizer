f=lambda g:[x for*x,in zip(*g)if(g!=(g:=x))*any(x)]
p=lambda g:f(f(g))