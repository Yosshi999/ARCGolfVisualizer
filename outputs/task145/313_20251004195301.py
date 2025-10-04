e=enumerate
def p(g):
 L=[]
 for i,v in e(g):
  for j,w in e(v):
   if j*(v[j-1]<1)+i*(g[i-1][j]<1)+w<1:
    k=i;l=j
    while k<len(g)and g[k][j]<1:k+=1
    while l<len(v)and v[l]<1:l+=1
    L+=((k-i)*(l-j),i,j,k,l),
 for s,i,j,k,l in L:
  for v in g[i:k]:v[j:l]=[(s==min(L)[0])*8+(s==max(L)[0])]*(l-j)
 return g