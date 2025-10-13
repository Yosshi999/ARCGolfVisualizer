f=lambda g,c:[sum(zip(*[v]*c),(2,))+(2,)for v in zip(*g)if{0}!={*v}!={0,2}]
p=lambda g:f(f(g,c:=sum(g,[]).count(2)//12),c)