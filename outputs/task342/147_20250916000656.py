def p(g):
 h=[[0]*10for _ in g];i,j=divmod(sum(g,[]).index(8),10)
 for k in-1,1:h[i+(k>0)][j:j+2]=filter(int,map(max,*g[i+k+(k>0)::k]*2))
 return h