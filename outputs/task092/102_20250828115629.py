f=lambda g:[[max({*v[:i]}&{*v[i:]}|{0})or v[i]for v in g]for i in range(len(g[0]))]
p=lambda g:f(f(g))