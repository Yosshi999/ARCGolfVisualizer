e=enumerate
def p(g):
 s={0}
 for i,v in e(g):
  m=0
  for j,w in e(v):m=(w>8)*(m+1);l=m//2;s|={(i+x,j+y)for x in range(-l,l+1)for y in range(-3*l+1,l+1)}
 return[[x or((i,j)in s)*3or 9in w[:i]for j,(*w,x)in e(zip(*g,v))]for i,v in e(g)]