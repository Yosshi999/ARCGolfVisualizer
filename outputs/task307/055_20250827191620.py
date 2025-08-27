f=lambda g:[*zip(*sum(zip(g,g),()))]
p=lambda g:f(f(g))