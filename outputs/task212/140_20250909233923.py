f=lambda g:[[w[i]or(1in w and i<w.index(1)<w.index(5))+(2in w[:i])*(5in w[i:])*2for w in zip(*g)]for i in range(9,-1,-1)]
p=lambda g:f(f(g))