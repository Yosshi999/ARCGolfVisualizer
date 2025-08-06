def f(g):
 g=[*map(list,zip(*g))]
 x=[]
 for i,v in enumerate(g):
  if len(set(v))==3:x+=[i]
 for i in x[1:-1]:
  j=0
  while g[i][j]==0:j+=1
  while g[i][j]>0:j+=1
  while g[i][j]==0:
   g[i][j]=8;j+=1
 return g
p=lambda g:f(f(g))