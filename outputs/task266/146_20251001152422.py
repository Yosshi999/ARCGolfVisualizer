def p(g):
 g[i:=g.index(v:=max(g))][j:=v.index(2)]=0
 for z in range(4):
  if 3>(x:=i+z//2*2-1)>-1<(y:=j+z%2*2-1)<5:g[x][y]=(3,6,8,7)[z]
 return g