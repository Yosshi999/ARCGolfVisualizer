def p(g):
 for s in[4,3]:
  I=J=H=0
  for i in range(len(g)-s+1):
   for j in range(len(g[0])-s+1):
    h=[v[j:j+s]for v in g[i:i+s]]
    if 0 not in sum(h,[]) and len({*sum(h,[])})>1:I=i;J=j;H=h
  if H==0:continue
  for v in g[I:I+s]:v[J:J+s]=[0]*s
  c=max(sum(g,[]))
  q=[[a for*w,a in zip(*g,v)if c in w]for v in g if c in v]
  d=len(q)//s
  return [[a*(b>0)for a,b in zip(v,w[::d])]for v,w in zip(H,q[::d])]