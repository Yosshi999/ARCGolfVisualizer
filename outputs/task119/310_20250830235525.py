E=enumerate
def p(g):
 for i,v in E(g):
  for j,w in E(v):
   if(11-i)*(11-j)*i*j>0<2==max(g[i-1][j],g[i][j-1],g[i+1][j],g[i][j+1])and w in[0,8]and[W for a,V in E(g)for b,W in E(V)if abs(i-a)==abs(j-b)].count(8)>1:
    for a,V in E(g):
     for b,W in E(V):
      if abs(i-a)==abs(j-b):g[a][b]=W or 3
 return g