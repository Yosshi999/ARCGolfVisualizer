def p(g):
 t=[[g[j][i]for j in range(6)]for i in range(3)]
 for i in range(3):
  if t[i][:3]==t[i][3:]:t[i]+=t[i][:3]
  else:t[i]+=t[i][2:5]
 return [[t[j][i]*2for j in range(3)]for i in range(9)]