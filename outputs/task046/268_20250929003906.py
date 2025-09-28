def p(g):
 g=[*zip(*g)]
 Y=[]
 a=[]
 for*v,in g+[min(g)]*any(g[-1]):
  if any(v):a+=v,
  else:
   c=sum({*sum(a,[])})-5
   if 5 in a[0]:a[0][f:=a[0].index(5)]=c;a=[v[f-t:]+v[:f-t]for v in a]
   if 5 in a[-1]:a[-1][t:=a[-1].index(5)]=c
   Y+=a
   a=[]
 return[*zip(*Y)]