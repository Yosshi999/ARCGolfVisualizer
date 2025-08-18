e=enumerate
def p(g):P,(Y,X),R=[(i,j)for i,v in e(g)for j,x in e(v)if x];return[[g[Y][X]*(max(abs(j-X),abs(i-Y))%(P[0]-Y)==0)for j,x in e(v)]for i,v in e(g)]