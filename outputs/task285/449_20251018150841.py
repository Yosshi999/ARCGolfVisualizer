R=range
def D(g,y,x,c):
 if len(g[0])>x>-1<y<len(g)>0<c==g[y][x]:g[y][x]-=99;return sum((D(g,y+a%3-1,x+a//3-1,c)for a in R(9)),[(y,x)])
 return[]
def q(g):
 for i in R(len(g)-2):
  for j in R(len(g[0])-2):
   if len(set(g[i+1][j+1:j+3]+g[i+2][j+1:j+3]))>3>0<g[i+1][j+1]:
    for u,v in D([*map(list,g)],i+1,j+1,g[i+1][j+1]):g[2*i+3-u][v]|=g[i+2][j+1];g[u][2*j+3-v]|=g[i+1][j+2]
 return [*map(list,zip(*g[::-1]))]
p=lambda g:q(q(q(q(q(q(q(q(g))))))))