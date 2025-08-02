def p(g):
 s = [[0 for i in range(3)]for j in range(3)]
 h = 0
 for i in range(len(g)-1):
  for j in range(len(g[0])-1):
   if g[i][j]*g[i][j+1]*g[i+1][j]*g[i+1][j+1]:
    s[h//3][h%3]=1
    h += 2
 return s