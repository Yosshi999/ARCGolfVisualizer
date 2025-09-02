def f(g):
 W=len(g[0])-1;Y=[]
 for i,v in enumerate(g):
  if v[0]>1:
   if v.count(8)==1:c=v.index(8);g[i]=[2]+[8]*(c-1)+[4]+[0]*(W-c)
   Y+=8 in v,
  if v[-1]==2and Y and Y.pop(0):g[i]=[8]*W+[2]
 return[v[::-1]for v in g]
p=lambda g:f(f(g))