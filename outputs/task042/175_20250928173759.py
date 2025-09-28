r=range(10)
def p(g):
 n=sum(sum(g,[]))//24+1
 for _ in[0]*4:g=[[g[i][j]|8*(10-i>2*n<=j>=g[i+n][j-n]<g[i+n][j-2*n]==3==g[i+2*n][j-n])for i in r]for j in r];g=g[::-1]
 return g