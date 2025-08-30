e=enumerate
def p(g):
 L=[]
 for i,v in e(g):
  for j,w in e(v):
   if j*(v[j-1]<1)+i*(g[i-1][j]<1)+g[i][j]<1:
    k=i;l=j
    while k<len(g)and g[k][j]<1:k+=1
    while l<len(v)and v[l]<1:l+=1
    print(i,j,k,l)
    L+=((k-i)*(l-j),i,j,k,l),
 (a,*_),*_,(b,*_)=sorted(L)
 print(a,b)
 for s,i,j,k,l in L:
  for v in g[i:k]:v[j:l]=[(s==a)*8+(s==b)]*(l-j)
 return g