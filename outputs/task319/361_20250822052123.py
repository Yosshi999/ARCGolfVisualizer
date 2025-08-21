E=enumerate
R=range(-32,14)
def p(g):
 *A,Z=sorted([[(i,j)for i,v in E(g)for j,x in E(v)if x==y]+[y]for y in range(10)],key=len)
 for*a,k in A[-3:]:
  for Y in R:
   for X in R:
    if min(H:={x-99*(((i-Y)//2,(j-X)//2)in a)for i,v in E(g)for j,x in E(v)})<0<len({*H})<5:V,H=zip(*a);return[[(Z[-1],k)[x==k]for x in v[min(H):max(H)+1]]for v in g[min(V):max(V)+1]]