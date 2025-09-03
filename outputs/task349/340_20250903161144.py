t=lambda g:[*zip(*g)]
e=enumerate
r=range
def p(g):
 g=t([[a|1if 9in v[:x]else a for x,a in enumerate(v)]for v in t(g)]);s={0}
 for y,v in e(g):
  for x,a in e(v):w=max(d for d in r(9)if d*(9,9)in[v[x:x+d*2],v[x-d*2+1:x+1]]);R=r(-w,w+1);s|={(q+y,p+x)for q in R for p in R if w}
 return[[a|((y,x)in s)*3*(a<9)for x,a in e(v)]for y,v in e(g)]