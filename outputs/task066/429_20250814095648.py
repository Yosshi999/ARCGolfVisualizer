e=enumerate
C=lambda g:[[*v]for v in g]
def f(g,y,x,q,p,d):
 if d<0 or not(0<=y+q<len(g) and 0<=x+p<len(g[0])):return
 if (t:=g[y+q][x+p])>7:return f(C(g),y,x,p:=p&1,q:=q&1,d-1)or f(g,y,x,-p,-q,d-1)
 if t==2:return g
 g[y+q][x+p]=3
 return f(g,y+q,x+p,q,p,d)

def p(g):
 [[D:=g[(Y:=y)+1][X:=x]==3for x,a in e(v[:-1])if a==3and 3in[g[y+1][x],g[y][x+1]]]for y,v in e(g[:-1])]
 return f(C(g),Y+D,X+(1-D),D,1-D,2)or f(g,Y,X,-D,D-1,2)