def p(g):
 h=[*zip(*g)]
 I=g.index
 m=I(max(g))
 M=I(max(g),m+1)
 J=h.index
 n=J(max(h))
 N=J(max(h),n+1)
 return[[max(max(g))*(v>0)for v in u[n+1:N]]for u in g[m+1:M]]