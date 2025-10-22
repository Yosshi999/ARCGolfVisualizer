r=range
def p(g):
 G=sum([[0,0]+v for v in g],[]);W=len(g[0])+2;s=[z for z in r(len(G)) if G[z]*any(1 in G[z+W*d-1:z+W*d+2]for d in r(-1,2))]
 for d in[3,2,1]:
  for Z in r(len(G)):
   b=1
   for z,c,_ in[(o:=(z*d+Y*W+X+Z)%len(G),G[z],b:=b&(G[o]==G[z]&2)&~(o in s))for Y in r(d)for X in r(d)for z in s]:G[z]|=b*(c+9)
 return[[a%9for a in G[y*W+2:y*W+W]]for y in r(len(g))]