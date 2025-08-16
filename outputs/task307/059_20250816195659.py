f=lambda g:sum([[v]*2for v in g],[])
p=lambda g:f(map(f,g))