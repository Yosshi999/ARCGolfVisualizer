def p(g):
 a=max([[a for a,b in zip(v,[0]+v)if a!=b]for v in g],key=len);s=len(a);c=s//2;r=range(s)
 return [[a[c-max(abs(i-c),abs(j-c))]for j in r]for i in r]