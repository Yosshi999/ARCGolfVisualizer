def p(g):
 r=range(9);u,l=min((i,j)for i in r for j in r if g[i][j]);c,*_={*sum(g,[])}-{0,2}
 for i in r:
  for j in r:
   if(g[u][l]==2)*(abs(i-j-u+l)<2)*(i<=u)*(j<=l):g[i][j]=g[i][j]or c
   if(g[u+1][l]==2)*(abs(i+j-1-u-l)<2)*(i>=u)*(j<=l):g[i][j]=g[i][j]or c
   if(g[u][l+1]==2)*(abs(i+j-1-u-l)<2)*(i<=u)*(j>=l):g[i][j]=g[i][j]or c
   if(g[u+1][l+1]==2)*(abs(i-j-u+l)<2)*(i>=u)*(j>=l):g[i][j]=g[i][j]or c
 return [[x if x in[0,c]else c for x in v]for v in g]