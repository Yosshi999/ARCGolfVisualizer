def p(g):
 Q=[];n=len(g)
 for i in range(n):Q+=(0,i),(i,0),(-1,i)
 for i,j in Q:
  if g[i][j]<1:g[i][j]=4;Q+=(i,~-j%n),(~-i%n,j),(-~i%n,j),(i,-~j%n)
 return[[(e^6)-2for e in v]for v in g]