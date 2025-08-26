r=range
def f(g,n):
 for t in r(9*9*n*n*2):
  if g[y:=t%9][x:=t//9%9]==3==g[y+1][x+1]>g[y][x+1]:
   for q,p in [(y-(Y:=t//81%n+n),x+(X:=t//81//n%n+n+1)),(y+X,x-Y)]:
    if 0<=p<10>q>=0:g[q][p]=8
 return g[::-1]
def p(g):n=sum(map(sum,g))//24+1;return f(f(g,n),n)