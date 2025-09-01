r=range
e=enumerate
p=lambda g:[[5 if c==5 else sum((g[Y*4+y//4][X*4+x//4]==4)*(g[Y*4+y%4][X*4+x%4])for Y in r(3) for X in r(3))for x,c in e(v)]for y,v in e(g)]