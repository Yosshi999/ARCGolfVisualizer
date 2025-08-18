e=enumerate
def p(g):P,(Y,X,C),R=[(i,j,x)for i,v in e(g)for j,x in e(v)if x];return[[C*(max(j-X,i-Y,key=abs)%(P[0]-Y)==0)for j,x in e(v)]for i,v in e(g)]