def p(g):
 L=[]
 for i in range(12):
  for j in range(12):
   h=[v[j:j+3]for v in g[i:i+3]]
   if all(sum(v)*sum(w)for*w,v in zip(*h,h)):
    L.append(h)
 return max(L,key=L.count)