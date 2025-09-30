e=enumerate
def p(g,b=0):
 for i,v in e(g):
  for j,w in e(v):
   if w:
    if all(g[i-1][b+1:j])*i:l=j-b-1;v[b+1:j]=[2+l%2*5]*l
    b=j
 return g