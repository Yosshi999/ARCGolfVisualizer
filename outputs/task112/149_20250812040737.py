e=enumerate
def p(g):
 I,J=min((i,j)for i,v in e(g)for j,x in e(v)if x==3)
 return[[g[min(i,2*I+1-i)][min(j,2*J+1-j)]for j,_ in e(v)]for i,v in e(g)]