def has_hole(g,x):
 if l:=[(i,j)for i,v in enumerate(g)for j in range(len(v))if g[i][j]==x]:
  c,r=map(list,zip(*l))
  return(max(c)-min(c)+1)*(max(r)-min(r)+1)>len(c)
p=lambda g:[[x+1for x in range(9)if has_hole(g,x+1)]]