def f(g):
 Y=[]
 for i,r in enumerate(g):
  if r[0]==2:
   if r.count(8)==1:Y+=[1];c=r.index(8);g[i]=[2]+[8]*(c-1)+[4]+[0]*(len(r)-c-1)
   else:Y+=[0]
  if r[-1]==2and Y:
   if Y.pop(0):g[i]=[8]*(len(r)-1)+[2]
 return [v[::-1]for v in g]
p=lambda g:f(f(g))