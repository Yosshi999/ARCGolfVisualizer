def p(g):
 H={}
 for i in range(144):
  h=(*[(*v[i%12:i%12+3],)for v in g[i//12:i//12+3]],)
  if all(sum(v)>0for v in h)and all(sum(v)>0for v in zip(*h)):H[h]=H.get(h,0)+1
 return[*map(list,max(H,key=lambda k:H[k]))]