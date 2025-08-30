e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v):
   if w*any(6in u[j-(j>0):j+2]for u in g[i-(i>0):i+2])>7:v[j]=3
 return[[(a:=v[j],4)[6*(a!=6)in{*v[:j]}&{*v[j:]}&{*w[:i]}&{*w[i:]}]for j,w in e(zip(*g))]for i,v in e(g)]