def f(g):q=len(max(map(set,g)))-1;return[[(c*(c!=q),d)[d==q]for c,d in zip(v,[0]+v)]for*v,in zip(*g)]
p=lambda g:f(f(f(f(f(f(f(f(g))))))))