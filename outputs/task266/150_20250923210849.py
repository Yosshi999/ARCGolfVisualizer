def p(g):
 g[i:=g.index(v:=max(g))][j:=v.index(2)]=0
 for c,x,y in(3,i-1,j-1),(6,i-1,j+1),(8,i+1,j-1),(7,i+1,j+1):
  if 3>x>-1<y<5:g[x][y]=c
 return g