def p(g):
 f=lambda c:[[a for*w,a in zip(*g,v)if c in w]for v in g if c in v];r=f(2);n=len(r)-2;R=range(n)
 for i in R:
  for j in R:r[i+1][j+1]=f(sum({*sum(g,[])})-2)[3*i//n][3*j//n]
 return r