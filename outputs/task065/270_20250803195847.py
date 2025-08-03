def p(g):
 if len(g)==3:
  a=[0]*10
  a[g[0][0]]+=1
  a[g[2][0]]+=1
  a[g[0][2]]+=1
  a[g[2][2]]+=1
  return [[a.index(1)]]
 w=len(g)//2+1
 for i in [0,1]:
  for j in [0,1]:
   h=[v[j*w:j*w+w-1]for v in g[i*w:i*w+w-1]]
   if len(set(v for u in h for v in u))==2:return h