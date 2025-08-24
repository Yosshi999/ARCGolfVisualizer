f=lambda g:eval(f'{[*zip(*g[::-1])]}'.replace('3, 2','8, 0'))
p=lambda g:f(f(f(f(g))))