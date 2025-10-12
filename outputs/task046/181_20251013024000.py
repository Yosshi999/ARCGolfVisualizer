def p(g):
 g=[*zip(*g)];d=m=p=0;G=[]
 for y,(*v,)in enumerate(g):
  if 5in v:v[x:=v.index(5)]=sum({*v,*g[y+2*p-1]})-5;d+=(x-m)*p;p^=1;m=x
  G+=[v[d:]+v[:d]]*any(v)
 return[*zip(*G)]