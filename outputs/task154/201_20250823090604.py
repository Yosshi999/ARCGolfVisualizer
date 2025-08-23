t=lambda g:[*map(list,zip(*g))]
def p(g):
 f=5in max(g)
 g=(g,t(g))[f]
 i=g.index(max(g),4)
 z=[[0]*15]
 g=z*3+g[3:5]+g[:2][::-1]+z*(i==11)+g[i+2:i+4][::-1]+g[i-1:i+1]+z*(3+(i==10))
 return (g,t(g))[f]