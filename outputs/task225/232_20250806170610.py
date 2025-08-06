r=[0,1]
def p(g):
 z=[[0]*8]*2
 g=z+[[0,0,*v,0,0]for v in g]+z
 for k in range(64):
  if g[i:=k//8][j:=k%8]:
   for x in r:
    for y in r:J=j+2-4*y;g[I:=i+2-4*x][J:J+2]=g[I+1][J:J+2]=[g[i+x][j+y]]*2
   return[v[2:8]for v in g[2:8]]