f=lambda x:sum(zip(x,x,x),())
p=lambda g:f([*map(f,g)])