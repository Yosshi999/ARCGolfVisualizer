def p(g):
 c=len(set(v for u in g for v in u))-1
 return [sum([[w]*c for w in v],[])for v in g for _ in [0]*c]