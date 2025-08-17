def p(g):
 for k in range(64):
  i=k//8;j=k%8;s=slice(j,j+3)
  if g[i][s]==g[i+2][s]==[1]*3and g[i+1][s]==[1,0,1]:g[i][s]=g[i+2][s]=[0,2,0];g[i+1][s]=[2]*3
 return g