def p(g):
 g=[*zip(*g)];d=m=0;p=1;G=[]
 for y,(*v,)in enumerate(g):
  if(x:=bytes(v).find(5))>=0:d+=(x-m)*(p:=p^1);m=x;v[x],={*v,*g[y+2*p-1]}-{0,5}
  G+=[[0,0,*v,0,0][d+2:d+5]]*any(v)
 return[*zip(*G)]