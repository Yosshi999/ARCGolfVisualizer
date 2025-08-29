r=range
def p(j):
 E=len({*sum(j,[])})-1;R=r(5*E);g=[[j[W//E][l//E]for l in R]for W in R]
 for z in r(4*E):
  if(X:=z%2*3-(j[1][0]>0))>=0<=(Y:=z//2%2*3-(j[0][1]>0)):g[Y*E+z//4][X*E+z//4+(0<z%4<3)*(E-z//4*2-1)]=2
 return g