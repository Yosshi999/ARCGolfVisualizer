e=enumerate
def p(g):
 h=[[{(i*99+j+1)*(w==2)}for j,w in e(v)]for i,v in e(g)]
 for _ in[0]*99:
  for i,v in e(g):
   for j,w in e(v):
    if j and w*g[i][j-1]:h[i][j]=h[i][j-1]=h[i][j]|h[i][j-1]
    if i and w*g[i-1][j]:h[i][j]=h[i-1][j]=h[i][j]|h[i-1][j]
 return[[8*(len(max(sum(h,[]),key=len))==9)]]