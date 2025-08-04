r=[-1,0,1]
def p(g):
 p=0
 for i in range(len(g)):
  for j in range(1,len(g[0])):
   def f(c):
    for x in r:
     for y in r:g[i+x][j+y]=c
    g[i][j]=3
   if p*g[i][j]==3:f(2);return g
   if g[i][j-1:j+2]==[2,3,2]:f(0);p=1