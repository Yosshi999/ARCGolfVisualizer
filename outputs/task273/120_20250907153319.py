e=enumerate
p=lambda g:[[v[j]or(sum(sum(u[:j])for u in g[:i])%16==4>max(v+w))*2for j,(*w,)in e(zip(*g))]for i,v in e(g)]