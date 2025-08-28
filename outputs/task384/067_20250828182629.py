f=lambda g:[*filter(max,zip(*sum(zip(g,g),())))]
p=lambda g:f(f(g))