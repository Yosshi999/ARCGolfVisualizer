def f(g):b=0;return[*map(list,zip(*[x for x in g if b!=(b:=x)]))]
p=lambda g:f(f(g))