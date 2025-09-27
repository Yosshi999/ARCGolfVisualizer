def p(g):
 g=[[0,*v,0]for v in g*2]
 i,j=divmod(sum(g,[]).index(2),7)
 g[i][j]=0;g[i-1][j-1:j+2]=[3,0,6];g[i+1][j-1:j+2]=[8,0,7]
 return[v[1:6]for v in g[:3]]