def p(g):
 G=sum(g,[]);C=max(G[:3]+G[10:13]);F=G.index
 G=[(c,5)[all((G[z]==c!=C)==(G[z+F(C)-F(c)]==C)for z in range(100))]for c in G]
 return[*zip(*[iter(G)]*10)]