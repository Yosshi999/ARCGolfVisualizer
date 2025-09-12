r=range
e=enumerate
def p(g):
 C,={*sum(g,[])}-{0,5}
 for d in[0,1]:
  P={y-x+1 for y in r(9)for x in r(9)if g[y][x:x+2]+g[y+1][x:x+2]==[0,5,0,0]}
  g=[[(c*d!=5)*(c|(C*(x-y in P)))for x,c in e(v)]for y,v in e(zip(*g))]
 return g