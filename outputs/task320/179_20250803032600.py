def p(g):
 a=[0]*4
 for i in range(len(g)):
  for j in range(4):
   if a[j]<1and g[i][j*2+1]>0:
    a[j]=(len(g)-i)//2
   if a[j]>0and i>len(g)-1-a[j]:
    g[i][j*2+1]=8
 return g