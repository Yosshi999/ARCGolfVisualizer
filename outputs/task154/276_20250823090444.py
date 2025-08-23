t=lambda g:[*map(list,zip(*g))]
def p(g):
 f=5in max(g)
 g=(g,t(g))[f]
 i=g.index(max(g),4)
 assert(i in [10,11])
 z=[[0]*15]
 if i==11:
  g=z*3+g[3:5]+g[:2][::-1]+z+g[13:][::-1]+g[10:12]+z*3
 if i==10:
  g=z*3+g[3:5]+g[:2][::-1]+g[12:14][::-1]+g[9:11]+z*4
 return (g,t(g))[f]