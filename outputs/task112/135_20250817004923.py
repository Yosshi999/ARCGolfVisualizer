e=enumerate
def p(g):I,J=divmod(sum(g,[]).index(3),len(g[0]));return[[g[min(i,2*I+1-i)][min(j,2*J+1-j)]for j,_ in e(v)]for i,v in e(g)]