r=range
def p(g):
 for K in range(81):
  if g[I:=K//9][J:=K%9]:
   for k in r(4):
    x=k//2*2-1;y=k%2*2-1
    if g[i:=I+k//2][j:=J+k%2]==2:
     for a,b in[(x,0),(-x,y),(x,0)]*9:
      if 9>i>-1<j<9:g[i][j]=sum({*sum(g,[])}-{2})
      i+=a;j+=b
   return g