E=enumerate
R=range(-36,18)
def p(g):
 G={(i,j):x for i,v in E(g)for j,x in E(v)}
 *_,A,B,C,(*_,c)=sorted([[(i,j)for(i,j),x in G.items()if x==y]+[y]for y in range(10)],key=len)
 for*a,k in A,B,C:
  for Y in R:
   for X in R:
    if min(H:={x-99*(((i-Y)//2,(j-X)//2)in{*a})for(i,j),x in G.items()})<0and len({*H})==4:
     print(f"{a=} {(Y,X)=} {set(H)=}")
     (u,*_,d),(l,*_,r)=map(sorted,zip(*a))
     return[[(c,k)[x==k]for x in v[l:r+1]]for v in g[u:d+1]]