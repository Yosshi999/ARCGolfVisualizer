def p(g):
 H={}
 for i in range(12):
  for j in range(12):
   h=(*[(*v[j:j+3],)for v in g[i:i+3]],)
   if all(sum(v)>0for v in h)and all(sum(v)>0for v in zip(*h)):
    H[h]=H.get(h,0)+1
 return [[*v]for v in max(H,key=lambda k:H[k])]