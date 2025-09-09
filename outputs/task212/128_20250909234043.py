f=lambda g:[[w[i]or(5in w[i:])*((1in w[i:w.index(5)])+(2in w[:i])*2)for w in zip(*g)]for i in range(9,-1,-1)]
p=lambda g:f(f(g))