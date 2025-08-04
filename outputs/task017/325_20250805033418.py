r=range(21);R=range(10)
def p(g):
 for m in range(4,10):
  for l in range(4,m+1):
   for o in range(1,l+1):
    h=[[g[i][j]for i in r for j in r if g[i][j]and (((i+o)%l-l//2)**2+((j+o)%l-l//2)**2)%m==d]for d in R]
    if all(len(set(v))<2for v in h):return[[h[(((i+o)%l-l//2)**2+((j+o)%l-l//2)**2)%m][0]for j in r]for i in r]