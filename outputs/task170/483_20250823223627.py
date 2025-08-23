def p(g):
 for s in[4,3]:
  I=J=H=0
  for i in range(len(g)-s+1):
   for j in range(len(g[0])-s+1):
    h=[v[j:j+s]for v in g[i:i+s]]
    if 0 not in sum(h,[]) and len({*sum(h,[])})>1:
     I=i
     J=j
     H=h
  if H==0:
   continue
  for x in range(s):
   for y in range(s):
    g[I+x][J+y]=0
  c=max(range(1,10),key=sum(g,[]).count)
  q=[[a for*w,a in zip(*g,v)if c in w]for v in g if c in v]
  return [[H[i][j]*(q[len(q)//s*i][len(q)//s*j]>0)for j in range(s)]for i in range(s)]