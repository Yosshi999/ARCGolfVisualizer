R=range(3)
def p(g):
 o=[*map(list,g)];v=[];s={(i,j)for i in R for j in R if g[i][j]}
 for a in range(100):
  if(i:=a//10,j:=a%10)not in v and o[i][j]!=max(f:=sum(g,[]),key=f.count):
   c=[(i,j)]
   for x,y in c:
    for d,e in(-~x%10,y),(~-x%10,y),(x,-~y%10),(x,~-y%10):
     if (d,e)not in c and o[d][e]==o[i][j]:c+=[(d,e)]
   v+=c
   if{(x-min(c)[0],y-min(c)[1])for x,y in c}=={(i-min(s)[0],j-min(s)[1])for i,j in s}:
    for x,y in c:o[x][y]=5
 for i in R:o[i][:3]=g[i][:3]
 return o