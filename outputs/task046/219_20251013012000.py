def p(g):
 g=[*zip(*g)]
 m=p=d=0
 G=[]
 for y,(*v,)in enumerate(g):
  x=bytes(v).find(5)
  if x>=0:
   if(p:=p^1):m=x-d
   else:d=x-m
   v[x],={*v,*g[y+1-p*2]}-{0,5}
  G+=[[0,0,*v,0,0][d+2:d+5]]*any(v)
 return[*zip(*G)]