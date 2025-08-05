f=lambda x:len(set(x))
def p(g):
 v=max(g[0],g[-1],key=f);w=max([v[0]for v in g],[v[-1]for v in g],key=f)
 if f(v)<f(w):return[[c]*~-f(w)for c in w if c]
 return[[*filter(None,v)]]*~-f(v)