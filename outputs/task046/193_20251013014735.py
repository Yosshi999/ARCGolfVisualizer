def p(g):
 g=[*zip(*g)];d=2;m=p=1;G=[]
 for y,(*v,)in enumerate(g):
  if 5in v:v[x:=v.index(5)],={*v,*g[y-2*p+1]}-{0,5};d+=(x-m)*(p:=p^1);m=x
  G+=[[0,0,*v,0,0][d:d+3]]*any(v)
 return[*zip(*G)]