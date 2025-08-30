E=enumerate
def p(g):
 for i,v in E(g):
  for j,w in E(v):
   if(11-i)*(11-j)*i*j<2<w:I,J=i,j
 for i,v in E(g):
  for j,w in E(v):
   if(11-i)*(11-j)*i*j>1==[g[i][j-1],g[i-1][j],g[i+1][j],g[i][j+1]].count(2)==(abs(i-I)==abs(j-J)):return[[W or(abs(i-a)==abs(j-b))*3for b,W in E(V)]for a,V in E(g)]