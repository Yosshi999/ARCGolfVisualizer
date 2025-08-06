e=enumerate
def p(g):
 p=0
 for i,v in e(g):
  for j,w in e(v):
   def f(c):
    for z in g[i-1:i+2]:z[j-1:j+2]=[c]*3
    v[j]=3
   if p*w==3:f(2);return g
   if v[j-1:j+2]==[2,3,2]:f(0);p=1