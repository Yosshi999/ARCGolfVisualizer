def p(g):
 a=max([[e for i,e in enumerate(v)if i==0 or e-v[i-1]]for v in g],key=len);s=len(a);c=s//2;r=range(s)
 return [[a[c-max(abs(i-c),abs(j-c))]for j in r]for i in r]