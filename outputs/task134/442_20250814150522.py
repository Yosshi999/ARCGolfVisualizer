def p(g):
 for k in range(6,1,-1):
  for i in range(len(g)-3*k+1):
   for j in range(len(g[0])-3*k+1):
    h=[]
    for I in range(3):
     r=[]
     for J in range(3):
      if all(x>0for v in g[i+I*k:i+I*k+k]for x in v[j+J*k:j+J*k+k]):
       c=g[i+I*k][j+J*k];r+=[1]
      else:r+=[0]
     h+=[r]
    if all(sum(v)for v in h)and all(sum(v)for v in zip(*h)):
     C=set(sum(g,[]))-{0,c};d=list(C)[0]
     return [[v*d for v in u]for u in h]