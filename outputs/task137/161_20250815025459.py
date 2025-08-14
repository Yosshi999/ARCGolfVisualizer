e=enumerate
def p(g):P,Q,R=[(i,j)for i,v in e(g)for j,x in e(v)if x];Y,X=Q;return[[g[Y][X]*(max(abs(j-X),abs(i-Y))%abs(P[0]-Y)<1)for j,x in e(v)]for i,v in e(g)]