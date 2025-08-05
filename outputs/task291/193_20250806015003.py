def f(g,x):
 c,r=map(list,zip(*[(i,j)for i,v in enumerate(g)for j,y in enumerate(v)if y==x]))
 return(max(c)-min(c)+1)*(max(r)-min(r)+1)>len(c)
p=lambda g:[[max(x for x in sum(g,[])if f(g,x))]]