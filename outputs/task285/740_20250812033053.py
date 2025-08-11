# find center
def f(g):
 p=[]
 for i in range(len(g)-1):
  for j in range(len(g[0])-1):
   if len({g[i][j],g[i][j+1],g[i+1][j],g[i+1][j+1]})==4: p+=[(i,j)]
 return p

# dup pattern
E=[-1,0,1];D=[(i,j)for i in E for j in E]
def d(g,i,j):
 # bfs
 q=[[(i,j),(i,j+1),(i+1,j),(i+1,j+1)]]
 f=lambda q:[g[y][x]for y,x in q[0]]
 c=f(q)
 while[]<q:
  t,*Q=q
  if max(f(q))>0 and all((a in[0,b])for a,b in zip(f(q),c)):
   for C,P in zip(c,t):
    Y,X=P;g[Y][X]=-C
   for y,x in D:
    Q+=[[(t[0][0]-y,t[0][1]-x),(t[1][0]-y,t[1][1]+x),(t[2][0]+y,t[2][1]-x),(t[3][0]+y,t[3][1]+x)]]
    for a,b in Q[-1]:
     if not(0<=a<len(g)and 0<=b<len(g[0])): Q.pop()
  q=Q
 return[[abs(x)for x in v]for v in g]

def p(g):
 for i,j in f(g):
  g=d(g,i,j)
 return g