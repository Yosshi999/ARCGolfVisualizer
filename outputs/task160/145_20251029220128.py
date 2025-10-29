def p(g,k=0):
 j=k%8
 for x in[0,1,2]*all(sum(g[k//8+x][j:j+3])==3-x%2for x in[0,1,2]):g[k//8+x][j:j+3]=x%2*2,2,x%2*2
 return g*(k>62)or p(g,k+1)