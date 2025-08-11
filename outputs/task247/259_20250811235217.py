def p(g):
 m=[10]*10;c=[0]*10
 for i in range(len(g)):
  for j in range(len(g[0])):
   if (k:=g[i][j])>0:
    m[k]=min(m[k],j);c[k]+=1
 D={}
 for k in range(10):
  if c[k]==max(c):
   D[m[k]]=k
 h=[[D[i]]*max(c)for i in sorted(D)]
 return [*map(list,zip(*h))]