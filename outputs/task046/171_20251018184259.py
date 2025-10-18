def p(g):
 g,*G=[*zip(*g)],;d=m=p=y=0
 for*v,in g:
  if 5in v:v[x:=v.index(5)]=sum({*v,*g[y+2*p-1]})-5;d+=(x-m)*p;p^=1;m=x
  G+=[v[d:]+v[:d]]*any(v);y+=1
 return[*zip(*G)]