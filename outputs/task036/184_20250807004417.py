e=enumerate
def p(g):
 x=[]
 for c in{*sum(g,[])}:
  I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w==c])
  x+=[v[min(J):max(J)+1]for v in g[min(I):max(I)+1]],
 return min(x,key=len)