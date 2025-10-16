def f(g):
 d=4
 while 5in g[d]:d+=1
 L=[10*i+j for i in range(d)for j in range(10)if(5in{*g[i][:j]}&{*g[i][j:]})>g[i][j]]
 G=sum(g,[])
 for c in{*G}:
  P=[i for i in range(100)if G[i]==c]
  if len({*map(int.__sub__,L,P)})==1 and len(L)==len(P):
   for i in L:G[i]=c
   for i in P:G[i]=0
 return[*map(list,zip(*[iter(G)]*10))][::-1]
p=lambda g:f(f(g))