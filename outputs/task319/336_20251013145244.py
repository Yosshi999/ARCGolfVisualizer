E=enumerate
R=range(-32,14)
def p(g):
 *A,Z=sorted([[(i,j)for i,v in E(g)for j,x in E(v)if x==y]+[y]for y in R],key=len)
 for*a,k in A[-3:]:
  for Y in R:
   for X in R:
    if min(H:={x-99*(((i-Y)//2,(j-X)//2)in a)for i,v in E(g)for j,x in E(v)})<0<len({*H})<5:return[[(Z[-1],k)[x==k]for*w,x in zip(*g,v)if k in w]for v in g if k in v]