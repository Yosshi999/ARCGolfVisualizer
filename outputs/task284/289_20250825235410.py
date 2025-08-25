e=enumerate
def f(g):
 g=[*map(list,zip(*g))];i=g.index(v:=max(g))
 if len({*v})==3:m,M=[j for j,w in e(v)if w];c=(m+M)//2;a,b=v[m],v[M];g[i][m:M+1]=[a]*(c-m)+[0,0]+[b]*(M-c-1);g[i+2][c-1:c+3]=g[i-2][c-1:c+3]=[a,a,b,b];g[i+1][c-1:c+3]=g[i-1][c-1:c+3]=[a,0,0,b]
 return g
p=lambda g:f(f(g))