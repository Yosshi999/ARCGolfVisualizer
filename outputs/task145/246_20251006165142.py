e=enumerate
def p(g):
 L=[(len(h:=g[i:W.index(2,i)])*((l:=V.index(2,j))-j),h,j,l)for i,v in e(g)for j,w in e(zip(*g))if(V:=v+[2])[j-1]&(W:=w+(2,))[i-1]>v[j]]
 for s,h,j,l in L:
  for v in h:v[j:l]=[(s==min(L)[0])*8+(s==max(L)[0])]*(l-j)
 return g