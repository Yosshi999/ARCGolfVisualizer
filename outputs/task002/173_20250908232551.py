def p(g):
 Q=[(0,0),(0,-1)];n=len(g)
 for i,j in Q:
  if g[i][j]<1:g[i][j]=4;Q+=(i,j-1),(i-1,j),(-~i%n,j),(i,-~j%n),(0,i),(i,0),(-1,i)
 return[[(e^6)-2for e in v]for v in g]