e=enumerate
def p(g):
 for v in g:
  for j,w in e(v[:-1]):
   if w==v[j+1]>0:c=w
 for i,v in e(g):
  for j,w in e(v):
   t=f=0
   if i and g[i-1][j]:t+=1;f+=1
   if i<len(g)-1 and g[i+1][j]:t+=1;f+=1
   if j and v[j-1]:t+=1
   if j<len(g[0])-1 and v[j+1]:t+=1
   if w:v[j]=c*(t>2 or (t==2 and f==1))
 return g