f=lambda g:[x for x in g if g!=(g:=x)]
p=lambda g:f(map(f,g))