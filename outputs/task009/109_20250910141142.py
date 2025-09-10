e=enumerate
p=lambda g:[[max({*v[j::-3]}&{*v[j:]}|{*w[i::-3]}&{*w[i:]})for j,w in e(zip(*g))]for i,v in e(g)]