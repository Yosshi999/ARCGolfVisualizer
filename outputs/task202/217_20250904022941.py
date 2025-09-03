def f(g):
 M=[max(v)for v in zip(*g)]
 r=[]
 for v in g:
  z=[y for x,y in zip(v,M)if x==0]
  r+=[[x*(x not in z)for x in v]]
 return r
R=lambda g:[*zip(*g)]
p=lambda g:any(len({*v})<2 for v in g)and R(f(R(g)))or f(g)