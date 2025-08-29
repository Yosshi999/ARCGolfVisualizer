def f(v):
 for s,t in[(3,2),(7,1)]:
  if s in v and t in v and(a:=v.index(s))<(b:=v.index(t)):
   v[a]=0;v[b-1]=s
 return v
p=lambda g,d=4:p([f([*v])for v in zip(*g)][::-1],d-1)if d else g