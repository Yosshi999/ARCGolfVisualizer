r=range(10)
def p(g):
 for s in range(21):
  for t in range(s%2,21,2):
   f=lambda i,j:max(abs(s-2*i-1),abs(t-2*j-1))%(6-s%2*2)==3-s%2
   if all(f(i,j)for i in r for j in r if g[i][j]):return[[(5,max(sum(g,[])))[f(i,j)]for j in r]for i in r]