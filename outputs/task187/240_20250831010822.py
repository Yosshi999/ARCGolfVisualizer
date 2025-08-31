def p(g):
 Q=[];h=len(g);w=len(g[0])
 for i in range(h):Q+=(i,0),(i,w-1)
 for j in range(w):Q+=(0,j),(h-1,j)
 for i,j in Q:
  if g[i][j]<1:g[i][j]=3;Q+=(i,~-j%w),(~-i%h,j),((i+1)%h,j),(i,(j+1)%w)
 return[[e if e else 2for e in v]for v in g]