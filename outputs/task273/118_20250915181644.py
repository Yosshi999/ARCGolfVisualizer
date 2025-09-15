e=enumerate
p=lambda g:[[v[j]+(5>sum(sum(u[:j])for u in g[:i])%16>max(v+w))*2for j,(*w,)in e(zip(*g))]for i,v in e(g)]