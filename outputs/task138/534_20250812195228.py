def p(g):
 h=[*map(list,zip(*g))]
 I=[];J=[]
 for i in range(len(g)):
  if all(v>0for v in g[i]):I+=[i]
 for j in range(len(g[0])):
  if all(v>0for v in h[j]):J+=[j]
 G=[r[J[0]:J[1]+1]for r in g[I[0]:I[1]+1]]
 H=[*map(list,zip(*G))]
 c=0
 for i in range(1,len(G)-1):
  for j in range(1,len(G[0])-1):
   c=c or G[i][j]
 for i in range(1,len(G)-1):
  for j in range(1,len(G[0])-1):
   if c in G[i][1:j]and G[i][-1]==c or c in G[i][j:-1]and G[i][0]==c or c in H[j][1:i]and H[j][-1]==c or c in H[j][i:-1]and H[j][0]==c:G[i][j]=c
 return G