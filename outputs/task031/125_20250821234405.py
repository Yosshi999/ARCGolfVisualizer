#f=lambda g:[*map(list,zip(*filter(sum,g)))];p=lambda g:f(f(g))
p=lambda g:[*map(list,filter(max,zip(*filter(max,zip(*g)))))]