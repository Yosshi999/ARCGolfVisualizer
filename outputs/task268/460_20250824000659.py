e=enumerate
t=lambda g:[*map(list,zip(*g[::-1]))]
def f(g):
 if -1in sum(g,[]):return t(g)
 P=[(i,j)for i,v in e(g)for j,w in e(v)if w]
 a,b=min(P)
 if g[a][b+2]:return t(g)
 c,d=max(P)
 for v in g[a+1:c]:v[b+1:d]=[-1]*(d-b-1)
 for v in g[:a+1]:v[b+2:d-1]=[-1]*(d-b-3)
 x=a-1
 y=b+1
 while min(x,y)>=0:g[x][y]=-1;x-=1;y-=1
 x=a-1
 y=d-1
 while x>=0 and y<len(g[0]):g[x][y]=-1;x-=1;y+=1
 return t(g)
p=lambda g:[[4if w<0else w for w in v]for v in f(f(f(f(g))))]