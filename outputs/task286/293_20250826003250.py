r=range
def p(g):
 def D(y,x):
  if len(g[0])>x>-1<y<len(g)>0==g[y][x]:g[y][x]=s[(x+y)%2];[D(y+a%3-1,x+a//3-1)for a in r(9)]
 s=[0,0];X=[]
 for i in r(len(g)):
  for j in r(len(g[0])):
   if 0!=g[i][j]!=8:s[(i+j)%2]=g[i][j];X+=[(i,j)]
 for i,j in X:[D(i+a%3-1,j+a//3-1)for a in r(9)]
 return g