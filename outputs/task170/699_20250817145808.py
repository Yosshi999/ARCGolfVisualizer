def Q(g):
 for s in [4,3]:
  for i in range(len(g)+1-s):
   for j in range(len(g[0])+1-s):
    h=[r[j:j+s]for r in g[i:i+s]]
    if 0 not in sum(h,[]) and len(set(sum(h,[])))>1:
     for I in range(i,i+s+1):
      for J in range(j,j+s+1):
       g[I][J]=0
     return h
def p(g):
 H=Q(g)
 s=len(H)
 for k in [3,4,5]:
  for i in range(len(g)+1-k*s):
   for j in range(len(g[0])+1-k*s):
    b=1;F=[];G=[r[j:j+k*s]for r in g[i:i+k*s]]
    for I in range(s):
     E=[]
     for J in range(s):
      f={v for R in G[I*k:I*k+k]for v in R[J*k:J*k+k]}
      if len(f)>1:b=0
      if 0 in f:E+=[0]
      else:E+=[H[I][J]]
     F+=[E]
    if b and all(any(E)for E in F)and all(any(E)for E in zip(*F)):return F