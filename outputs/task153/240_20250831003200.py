r=range(10);R=range(3)
def p(g):
 z=[[0]*12];g=z+[[0]+v+[0]for v in g]+z
 for a in r:
  for b in r:
   for c in r:
    for d in r:
     w=[[g[i+a][j+b]|g[i+c][j+d]for j in R]for i in R];s={*sum(w,[])}
     if 0not in s and len(s)>1:return w