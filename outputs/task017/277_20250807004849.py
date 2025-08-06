r=range(21);R=range(10)
def p(g):
 for m in R[1:]:
  for l in R[1:]:
   for o in R:
    f=lambda i:((i+o)%l-l//2)**2;h=[[g[i][j]for i in r for j in r if g[i][j]and(f(i)+f(j))%m==d]for d in R]
    if all(len(set(v))<2for v in h):return[[h[(f(i)+f(j))%m][0]for j in r]for i in r]