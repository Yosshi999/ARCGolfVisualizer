R=range(12)
def p(g):
 (I,J),=[(i,j)for i in R for j in R if(11-i)*(11-j)*i*j<2<g[i][j]]
 for i in R:
  for j in R:
   if(11-i)*(11-j)*i*j>3>sum([g[i][j-1],g[i-1][j],g[i+1][j],g[i][j+1]])>(abs(i-I)==abs(j-J))>0:return[[g[a][b]or(abs(i-a)==abs(j-b))*3for b in R]for a in R]