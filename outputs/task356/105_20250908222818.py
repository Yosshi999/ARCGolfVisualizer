e=enumerate
p=lambda g:[[sum({*v[:j]}&{*v[j:]}|{*w[:i+1]}&{*w[i:]})for j,w in e(zip(*g))]for i,v in e(g)]