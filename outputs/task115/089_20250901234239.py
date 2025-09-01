f=lambda g:[*zip({w:0for w in v})]if max(v:=g[0])-min(v)else[*zip(*g)]
p=lambda g:f(f(g))