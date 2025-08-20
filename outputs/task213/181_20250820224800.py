f=lambda x:len({*x})
def p(g):
 if f(v:=max(g[0],g[-1],key=f))<f(w:=max([v[0]for v in g],[v[-1]for v in g],key=f)):return[[c]*~-f(w)for c in w if c]
 return[[*filter(int,v)]]*~-f(v)