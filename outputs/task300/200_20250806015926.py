def p(g):
 M=max((sum(g,[]).count(i),i)for i in range(1,10))[1]
 v,h=map(list,zip(*[(i,j)for i,v in enumerate(g)for j,y in enumerate(v)if y==M]))
 return[l[min(h):max(h)+1]for l in g[min(v):max(v)+1]]