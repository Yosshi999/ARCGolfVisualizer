f=lambda g:sum([[v]*4for v in g],[])
p=lambda g:f([f(v[1::2])for v in g[1::2]])