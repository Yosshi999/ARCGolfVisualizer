R=[-2,-1,0]
def p(g):
 for e in range(10000):
  w=[[g[i+e//1000][j+e//100%10]|g[i+e//10%10][j+e%10]for j in R]for i in R]
  if{*sum(w,[])}=={*sum(g,[])}-{0}:return w