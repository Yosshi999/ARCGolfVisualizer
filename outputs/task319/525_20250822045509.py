E=enumerate
R=range(-36,18)
def p(g):
 G={(i,j):x for i,v in E(g)for j,x in E(v)}
 *_,A,B,C,(*_,c)=sorted([[(i,j)for(i,j),x in G.items()if x==y]+[y]for y in range(10)],key=len)
 for*a,k in A,B,C:
  for y in R:
   for x in R:
    H=G.copy()
    for i,j in a:
     for b in range(4):
      z=(i*2+y+b//2,j*2+x+b%2)
      if z in H:H[z]-=99
    if min(v:=H.values())<0and len({*v})==4:
     print(f"{a=} {(y,x)=} {set(v)=}")
     (u,*_,d),(l,*_,r)=map(sorted,zip(*a))
     return[[(c,k)[x==k]for x in v[l:r+1]]for v in g[u:d+1]]