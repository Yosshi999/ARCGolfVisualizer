def p(g):
 h=[[0]*10for _ in g]
 for _ in'..':i,j=divmod(sum(g,[]).index(8),10);h[i][j:j+2]=filter(int,map(max,*g[:i]*2));g=g[::-1];h=h[::-1]
 return h