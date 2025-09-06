e=enumerate
f=lambda v,j:max({*v[j::-3]}&{*v[j::3]})
p=lambda g:[[max(f(v,j),f(w,i))for j,w in e(zip(*g))]for i,v in e(g)]