r=range
def p(j):
 E=len({*sum(j,[])})-1;g=[[j[W//E][l//E]for l in r(5*E)]for W in r(5*E)]
 for k in r(4):
  for n in r(E):
   if(X:=k%2*3-(j[1][0]>0))>=0<=(Y:=k//2*3-(j[0][1]>0)):g[Y*E+n][X*E+n+(0<k<3)*(E-2*n-1)]=2
 return g