def p(g):
 C=list(set(v for u in g for v in u)-{0,5})[0]
 for j in range(-9,10):
  K=0
  for i in range(10):
   I=i;J=i+j
   if 0<=J<10:
    if g[I][J]==5:K=9
    if I<9and J>0and g[I+1][J-1]==5or I>0and J<9and g[I-1][J+1]==5:K+=1
  if K==1:
   for i in range(10):
    if 0<=i+j<10:g[i][i+j]=C
 for i in range(10):
  for j in range(10):
   if g[i][j]==5:g[i][j]=0
 return g