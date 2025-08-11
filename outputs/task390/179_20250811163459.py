def t(v):
  if not(2 in v and 5 in v):return v
  k=v.index(2)
  return v[k+4:][::-1]+v[k-3:k+4]+v[:k-3][::-1]

f=lambda g:[*map(list,zip(*[t(t(v))for v in g]))]
p=lambda x:f(f(x))