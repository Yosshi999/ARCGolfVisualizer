r=range(9)
def p(g):
 a=b=9;c=d=0
 for i in r:
  for j in r:
   if g[i][j]:a=min(a,i);b=min(b,j);c=max(c,i);d=max(d,j)
 return[sum([[w]*2for w in v[b:d+1]],[])for v in g[a:c+1]for _ in[0,0]]