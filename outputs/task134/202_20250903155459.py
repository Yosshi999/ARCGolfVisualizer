def p(g):
 G=sum(g,[])
 for i,v in enumerate(G[1:-1]):
  if G[i]==G[i+2]==0<v:c=v
 d=sum({*G})-c;h=[[c*(a==d)for*w,a in zip(*g,v)if d in w]for v in g if d in v];e=len(h)//3;return[v[::e]for v in h[::e]]