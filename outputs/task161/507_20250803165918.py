def p(g):
 a=set();b=set()
 h=[[0]*len(u)for u in g]
 for i in range(len(g)):
  if g[i][0]==g[i][-1]:a|={g[i][0]}
  else:b|={g[i][0],g[i][-1]}
 for j in range(len(g[0])):
  if g[0][j]==g[-1][j]:a|={g[0][j]}
  else:b|={g[0][j],g[-1][j]}
 a=a-b
 a=list(a)[0]
 for i in range(len(g)):
  if g[i][0]==a:
   for j in range(len(g[i])):h[i][j]=g[i][0]
 g=[*map(list,zip(*g))]
 h=[*map(list,zip(*h))]
 for i in range(len(g)):
  if g[i][0]==a:
   for j in range(len(g[i])):h[i][j]=g[i][0]
 return [*map(list,zip(*h))]