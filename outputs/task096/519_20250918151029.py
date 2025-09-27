e=enumerate
def p(g):
 H=[]
 f=sum(g,[])
 C=max(f,key=f.count)
 D=[]
 P={}
 for d in range(10):
  for c in {*f}:
   L=[(i,j)for i,v in e(g)for j,w in e(v)if w==c]
   for x in range(20):
    for y in range(-1,19):
     if c not in D and all(max(abs(x-i),abs(y-j))==d and not (0<=2*x-i<len(g) and c!=g[2*x-i][j] or 0<=2*y-j<len(g[0]) and c!=g[i][2*y-j])for i,j in L):
      D+=c,
      H+=d,
      P|={(abs(i-x),abs(j-y)):c for i,j in L}
 l=max(H)
 *r,=map(abs,range(-l,l+1))
 return[[P.get((i,j),C)for j in r]for i in r]