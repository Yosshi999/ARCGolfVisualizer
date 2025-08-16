f=lambda g:sum(map(list,zip(g,g)),[])
p=lambda g:f([*map(f,g)])