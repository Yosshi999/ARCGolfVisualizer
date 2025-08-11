def t(v):
  if not(2 in v and 5 in v):return v
  k=v.index(2)
  r=v[:k-3]+v[k-3:k+4][::-1]+v[k+4:]
  print(k,v,r)
  return r[::-1]


f=lambda g:[*map(list,zip(*[t(t(v))for v in g]))]
p=lambda x:f(f(x))