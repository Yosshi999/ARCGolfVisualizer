e=enumerate
def p(g):I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w]);return[[(w,2)[w<(min(I)<=i<=max(I))*(min(J)<=j<=max(J))]for j,w in e(v)]for i,v in e(g)]