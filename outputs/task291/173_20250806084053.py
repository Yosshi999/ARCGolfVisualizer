e=enumerate
def f(g,x):c,r=zip(*[(i,j)for i,v in e(g)for j,y in e(v)if y==x]);return(max(c)-min(c)+1)*(max(r)-min(r)+1)>len(c)
p=lambda g:[[max(x*f(g,x)for x in sum(g,[]))]]