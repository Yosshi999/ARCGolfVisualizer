def p(g):
 o=[*map(list,g)];s={(i,j)for i in range(3)for j in range(3)if g[i][j]};t=s and{(i-min(s)[0],j-min(s)[1])for i,j in s}or{};b=max(sum(g,[]),key=sum(g,[]).count);v=[]
 for a in range(100):
  i,j=a//10,a%10
  if(i,j)not in v and o[i][j]!=b:
   c,q={(i,j)},[(i,j)]
   for x,y in q:
    for d,e in(x+1,y),(x-1,y),(x,y+1),(x,y-1):
     if 0<=d<10and 0<=e<10and(d,e)not in c and o[d][e]==o[i][j]:c|={(d,e)};q+=[(d,e)]
   v+=c
   if{(x-min(c)[0],y-min(c)[1])for x,y in c}==t:
    for x,y in c:o[x][y]=5
 for i in range(3):o[i][:3]=g[i][:3]
 return o