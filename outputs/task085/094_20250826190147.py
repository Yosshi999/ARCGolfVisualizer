e=enumerate
p=lambda g:[[w*(1-g[:i].count(v)*v[:j].count(w)%2)for j,w in e(v)]for i,v in e(g)]