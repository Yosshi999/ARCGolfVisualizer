def p(g):
 h=[[0]*9for _ in range(9)]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   G=[u[j:j+3]for u in g[i:i+3]]
   if all(v>0for u in G for v in u):
    if all(v==5for u in G for v in u):I,J=3,3
    elif G[1][1]==5:
     if G[0][0]!=5:I,J=0,0
     if G[0][2]!=5:I,J=0,6
     if G[2][0]!=5:I,J=6,0
     if G[2][2]!=5:I,J=6,6
    else:
     if G[0][1]!=5:I,J=0,3
     if G[1][0]!=5:I,J=3,0
     if G[2][1]!=5:I,J=6,3
     if G[1][2]!=5:I,J=3,6
    for u in range(3):
     for v in range(3):
      h[I+u][J+v]=G[u][v]
 return h