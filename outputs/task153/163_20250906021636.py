*r,=2,1,0
def p(g):
 for e in range(10000):
  w=[[g[e//1000-i][e//100%10-j]|g[e//10%10-i][e%10-j]for j in r]for i in r]
  if{*sum(w,[])}=={*sum(g,[])}-{0}:return w