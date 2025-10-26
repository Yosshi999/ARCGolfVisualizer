def p(g,k=0):
 i=k//8;j=k%8
 for x in[0,1,2]*all(g[i+x][j:j+3]==[1,~x%2,1]for x in[0,1,2]):g[i+x][j:j+3]=[c:=x%2*2,2,c]
 return g*(k>62)or p(g,k+1)