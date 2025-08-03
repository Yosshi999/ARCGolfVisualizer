def p(g):
 f=lambda x:0<=x<len(g)
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    for I in range(-30,30):
     if f(i-I)and f(j-I):g[i-I][j-I]=g[i][j]
     if f(i+I)and f(j-I):g[i+I][j-I]=g[i][j]
     if f(i-I)and f(j+I):g[i-I][j+I]=g[i][j]
     if f(i+I)and f(j+I):g[i+I][j+I]=g[i][j]
    return g