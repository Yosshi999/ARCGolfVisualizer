def f(g,i,j,w):
 if 0<=i<10>j>=0==g[i][j]:
  g[i][j]=w
  for a in(i,j-1),(i,j+1),(i-1,j),(i+1,j):f(g,*a,w)
def p(g):
 f(g,0,0,1)
 for a in range(4):f(g,4+a%2,4+a//2,2)
 f(g,9,9,3);return g