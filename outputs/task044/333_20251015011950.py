def p(g):
 d=4
 while 5in g[d]:d+=1
 G=sum(g,[])
 for q in(range(d),range(d,10)):
  L=[10*i+j for i in q for j in range(10)if(5in{*g[i][:j]}&{*g[i][j:]})>g[i][j]]
  for c in{*G}:
   P=[i for i in range(100)if G[i]==c]
   if len({*map(int.__sub__,L*2,P*2)})==1:
    for i in L:G[i]=c
    for i in P:G[i]=0
 return[*zip(*[iter(G)]*10)]