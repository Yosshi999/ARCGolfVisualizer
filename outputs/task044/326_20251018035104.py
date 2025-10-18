def p(g):
 d=4;G=sum(g,[])
 while 5in g[d]:d+=1
 for q in(range(d),range(d,10)):
  L=[10*i+j for i in q for j in range(10)if(5in{*g[i][:j]}&{*g[i][j:]})>g[i][j]]
  for c in{*G}:
   P=[i for i in range(100)if G[i]==c]
   if len({*map(int.__sub__,L*2,P*2)})==1:
    for i,j in zip(L,P):G[i]=c;G[j]=0
 return[*zip(*[iter(G)]*10)]