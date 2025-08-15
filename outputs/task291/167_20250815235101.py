e=enumerate
def f(g,x):f=[(i,j)for i,v in e(g)for j,y in e(v)if y==x];a,b=min(f);c,d=max(f);return(c-a+1)*(d-b+1)>len(f)
p=lambda g:[[max(x*f(g,x)for x in sum(g,[]))]]