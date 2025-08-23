e=enumerate
def p(g):
 H=[];f=sum(g,[]);C=max(f,key=f.count);D=[]
 for d in range(10):
  for c in {*f}:
   L=[(i,j)for i,v in e(g)for j,w in e(v)if w==c]
   for x in range(-10,40):
    for y in range(-10,40):
     if all(max(abs(x-i),abs(y-j))==d for i,j in L) and c not in D and not any(0<=2*x-i<len(g) and c!=g[2*x-i][j] or 0<=2*y-j<len(g[0]) and c!=g[i][2*y-j]for i,j in L):
      D.append(c)
      H.append((c,d,min(abs(x-i)+abs(y-j)for i,j in L)))
 m=max(v[1]for v in H);M=2*m+1;h=[[C]*M for _ in [0]*M]
 for c,d,q in H:
  for i in range(M):
   for j in range(M):
    if max(abs(i-m),abs(j-m))==d and abs(i-m)+abs(j-m)>=q:
     h[i][j]=c
 return h