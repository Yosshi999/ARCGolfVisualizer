f=lambda g:[v for*v,in zip(*g)if max(range(1,10),key=sum(g,[]).count)in v]
p=lambda g:f(f(g))