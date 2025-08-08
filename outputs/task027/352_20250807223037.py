def p(g):
 C=[]
 for H,W in [(9,9),(10,10)]:
   c=[[*v]for v in g];X=1
   for i in range(10):
    for j in range(10):
     if 0<=H-i<10 and 0<=W-j<10:
      if g[i][j]==0 and g[H-i][W-j]==1:c[i][j]=2
     else:
      if g[i][j]==1:X=0
   if X and sum(v==2 for u in c for v in u)>0:C+=[c]
 c=min(C,key=lambda c:sum(v==2 for u in c for v in u))
 return c