def p(g):
 c=[0]*10
 for u in g:
  for v in u:c[v]+=1
 s=sorted(c)[::-1]
 s=s[:s.index(0)]
 h=[[c.index(S)]*S + [0]*(max(c)-S) for S in s]
 return [*map(list,zip(*h))]