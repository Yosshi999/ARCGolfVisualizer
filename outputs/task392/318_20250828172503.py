def p(g):
 for s in range(21):
  for t in range(21):
   if s%2!=t%2:continue
   if all(max(abs(s-2*i-1),abs(t-2*j-1))%(6-s%2*2)==(3,2)[s%2]for i in range(10)for j in range(10)if g[i][j]):
    c=max(sum(g,[]))
    return[[(5,c)[max(abs(s-2*i-1),abs(t-2*j-1))%(6-s%2*2)==(3,2)[s%2]]for j in range(10)]for i in range(10)]