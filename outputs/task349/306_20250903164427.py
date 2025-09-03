t=lambda g:[*zip(*g)]
e=enumerate
r=range
def p(g):
 g=t([[a|1if 9in v[:x]else a for x,a in e(v)]for v in t(g)]);s={0}
 for y,v in e(g):
  m=0
  for x,a in e(v):m=(v[x]>8)*(m+1);w=m//2;s|={(q+y,p+x)for q in r(-w,w+1)for p in r(-w*3+1,w+1)if w}
 return[[a|((y,x)in s)*3*(a<9)for x,a in e(v)]for y,v in e(g)]