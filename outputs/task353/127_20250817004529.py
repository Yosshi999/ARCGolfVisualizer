d=divmod
def p(g):I=sum(g,[]).index;i,j=d(I(3),w:=len(g[0]));k,l=d(I(4),w);g[i][j]=0;g[i+(i<k)-(i>k)][j+(j<l)-(j>l)]=3;return g