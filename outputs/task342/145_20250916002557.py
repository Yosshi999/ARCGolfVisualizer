def p(g):
 h=[[0]*10for _ in g];i,j=divmod(sum(g,[]).index(8),10)
 for k in 0,1:h[i+k][j:j+2]=filter(int,map(max,*g[i+3*k-1::2*k-1]*2))
 return h