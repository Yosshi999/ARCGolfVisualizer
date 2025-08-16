R=range(3)
def p(g):
 o=[*map(list,g)];v=[]
 for a in range(100):
  if(i:=a//10,j:=a%10)not in v and o[i][j]!=max(f:=sum(g,[]),key=f.count):
   c=[(i,j)]
   for x,y in c:
    for d,e in(-~x%10,y),(~-x%10,y),(x,-~y%10),(x,~-y%10):
     if (d,e)not in c and o[d][e]==o[i][j]:c+=[(d,e)]
   v+=c;X,Y=zip(*c)
   if{(x-min(X),y-min(Y))for x,y in c}=={(i-(g[0][:2]==[0,0]),j)for i in R for j in R if g[i][j]}:
    for x,y in c:o[x][y]=5
 for i in R:o[i][:3]=g[i][:3]
 return o