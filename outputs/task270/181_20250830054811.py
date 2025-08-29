def f(v):
 for s,t in[(3,2),(7,1)]:
  try:
   if(a:=v.index(s))<(b:=v.index(t)):v[a]=0;v[b-1]=s
  except:v
 return v
p=lambda g,d=4:p([f([*v])for v in zip(*g)][::-1],d-1)if d else g