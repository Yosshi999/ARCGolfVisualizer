e=enumerate
def p(g):
 x=y=-1
 for i,v in e(g):
  for j,w in e(v):
   if w:
    if x<0:x=i;y=j
    else:n=(x+i)//2;m=(y+j)//2;g[n-1][m]=g[n+1][m]=3;g[n][m-1:m+2]=[3]*3;return g