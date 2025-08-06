def p(m,P=range):
 for c in P(len(m[0])):
  for r in P(len(m)):
   if m[r][c]:break
  else:continue
  for i in P(r,len(m)):m[i][c]=m[r][c]
 return m