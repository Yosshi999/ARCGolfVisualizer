def f(g,x):
 if l:=[(i,j)for i,v in enumerate(g)for j,y in enumerate(v)if y==x]:
  c,r=map(list,zip(*l))
  return(max(c)-min(c)+1)*(max(r)-min(r)+1)>len(c)
p=lambda g:[[x+1for x in range(9)if f(g,x+1)]]