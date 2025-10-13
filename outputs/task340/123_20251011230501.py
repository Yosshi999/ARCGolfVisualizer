def p(g):
 for _ in[0]*4:g=[v[::-1]+[10+n+m*(m in v),10+m]for m,n,*v in zip(*g)]
 return[[w*(w>10)%10for w in v]for v in g]