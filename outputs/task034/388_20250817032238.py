e=enumerate
def p(g):
 u,l=min((i,j)for i,v in e(g)for j,x in e(v)if x);c,*_={*sum(g,[])}-{0,2}
 g=[[g[i][j]or c*((g[u][l]==2)*(abs(i-j-u+l)<2)*(i<=u)*(j<=l)+(g[u+1][l]==2)*(abs(i+j-1-u-l)<2)*(i>=u)*(j<=l)+(g[u][l+1]==2)*(abs(i+j-1-u-l)<2)*(i<=u)*(j>=l)+(g[u+1][l+1]==2)*(abs(i-j-u+l)<2)*(i>=u)*(j>=l))for j,x in e(v)]for i,v in e(g)]
 return [[x if x in[0,c]else c for x in v]for v in g]