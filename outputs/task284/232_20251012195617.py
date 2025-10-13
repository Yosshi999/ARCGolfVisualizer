e=enumerate
def f(g):
 V=max(g)
 if len({*V})>2:m,M=[j for j,w in e(V)if w];C=m+M>>1;g=[[V[(m,M)[x>C]]*((m<=x<=M>0==y)|(-3<y<3>x-C>-2)>(-2<y<2>x-C>-1))for x,c in e(v)]for y,v in e(g,-g.index(V))]
 return[*zip(*g)]
p=lambda g:f(f(g))