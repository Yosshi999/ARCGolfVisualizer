e=enumerate
def f(g):
 g=[*map(list,zip(*g))];i=g.index(v:=max(g))
 if len({*v})>2:m,M=[j for j,w in e(v)if w];c=m+M>>1;a,b=v[m],v[M];s=slice(c-1,c+3);v[m:M+1]=[a]*(c-m)+[0,0]+[b]*(M-c-1);g[i+2][s]=g[i-2][s]=[a,a,b,b];g[i+1][s]=g[i-1][s]=[a,0,0,b]
 return g
p=lambda g:f(f(g))