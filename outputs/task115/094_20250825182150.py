f=lambda g:[[x]for x in v if g!=(g:=x)]if max(v:=g[0])-min(v)else[*zip(*g)]
p=lambda g:f(f(g))