def p(g):
 for i in range(10):
  for j in range(10):
   if g[i][j]==5:
    I=i+1
    while I<10 and g[I][j+1]!=5:
     J=j+1
     while J<10 and g[I][J]!=5:
      g[I][J]=8;J+=1
     J=j+1
     while J>=0 and g[I][J]!=5:
      g[I][J]=8;J-=1
     I+=1
    J=j+1
    while J<10 and g[i+1][J]!=5:
     I=i+1
     while I<10 and g[I][J]!=5:
      g[I][J]=8;I+=1
     I=i+1
     while I>=0 and g[I][J]!=5:
      g[I][J]=8;I-=1
     J+=1
    return g