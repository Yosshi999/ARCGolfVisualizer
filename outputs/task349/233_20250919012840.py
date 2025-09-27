e=enumerate
def p(g):
 s={(i+x,j+y)for i,v in e(g)if~(m:=0)for j,w in e(v)if(m:=w//9*-~m)+(l:=m//2)+1for x in range(-l,l+1)for y in range(-3*l+1,l+1)}
 return[[x or((i,j)in s)*3or 9in w[:i]for j,(*w,x)in e(zip(*g,v))]for i,v in e(g)]