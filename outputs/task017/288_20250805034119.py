r=range(21);R=range(10)
def p(g):
 for m in R[1:]:
  for l in R[1:]:
   for o in R:
    f=lambda i,j:(((i+o)%l-l//2)**2+((j+o)%l-l//2)**2)%m;h=[[g[i][j]for i in r for j in r if g[i][j]and f(i,j)==d]for d in R]
    if all(len(set(v))<2for v in h):return[[h[f(i,j)][0]for j in r]for i in r]