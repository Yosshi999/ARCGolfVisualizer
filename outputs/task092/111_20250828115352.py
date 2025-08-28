f=lambda g:[[max(max({*v[:i]}&{*v[i:]}|{0})*11,v[i])%10for v in g]for i in range(len(g[0]))]
p=lambda g:f(f(g))