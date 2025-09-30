f=lambda g:[[sum({*v[:i]}&{*v[i:]})or v[i]for v in g]for i in range(len(g[0]))]
p=lambda g:f(f(g))