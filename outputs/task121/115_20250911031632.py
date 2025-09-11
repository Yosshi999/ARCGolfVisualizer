def p(g):
 for z in range(121):
  t=[v[z%11:][:3]for v in g[z//11:][:3]]
  if t[1][1]==8:t[1][1]=max(t[0]);return t