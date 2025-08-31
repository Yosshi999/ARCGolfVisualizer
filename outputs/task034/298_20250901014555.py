e=enumerate
r=range
def p(g):
 u,l=min((i,j)for i,v in e(g)for j,x in e(v)if x)
 c,*_={*sum(g,[])}-{0,2};S=[]
 for k in r(4):
  Y=k//2*2-1;X=k%2*2-1
  if g[y:=u+k//2][x:=l+k%2]==2:
   for k in r(9):S+=(y+k*Y,x+k*X),(y+k*Y-Y,x+k*X),(y+k*Y,x+k*X-X)
 for y,x in S:
  if 9>y>=0<=x<9:g[y][x]=c
 return g