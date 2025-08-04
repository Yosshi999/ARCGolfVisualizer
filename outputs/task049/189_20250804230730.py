def p(g):
 a=[]
 for c in range(10):
  X=[sum(v==c for v in u) for u in g]
  if len(set(X)-{0})==1 and sum(X)>0:a.append((sum(X),c,sum(v>0 for v in X)))
 S,c,H=min(a)
 return [[c]*(S//H)]*H