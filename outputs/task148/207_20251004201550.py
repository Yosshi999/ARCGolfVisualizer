def f(g):
 W=len(g[0])-1;Y=[]
 for v in g:
  if v[0]:
   if sum(v)==10:c=v.index(8);v[1:c+1]=[8]*~-c+[4]
   Y+=8in v,
  if v[-1]&2and Y and Y.pop(0):v[:-1]=[8]*W
 return[v[::-1]for v in g]
p=lambda g:f(f(g))