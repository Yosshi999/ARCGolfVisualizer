f=lambda g:[[max(v[j%(d:=(len(v)-v.count(0)-2)%99+2)::d])for j in range(len(v))]for v in zip(*g)]
p=lambda g:f(f(g))