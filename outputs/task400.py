def p(g):
 h = []
 for i in range(24):
  for j in range(24):
   if g[i][j] == 1:
    h.append(list(set([g[-i-1][j], g[-i-1][-j-1], g[i][-j-1]]) - set([1]))[0])
 return [h[i*5:i*5+5]for i in range(5)]