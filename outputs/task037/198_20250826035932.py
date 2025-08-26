E=enumerate
def p(g):
 s={}
 for i,v in E(g):
  for j,x in E(v):
   if x:s.setdefault(x,[]).append((i,j))
 for x in s:
  (u,a),(d,b)=sorted(s[x])
  for i,v in E(g[u:d]):v[(a+i,a-i)[b<a]]=x
 return g