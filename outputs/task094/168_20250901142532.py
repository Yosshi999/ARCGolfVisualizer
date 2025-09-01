def p(g):
 for k in range(121):g[i:=k//11+2][j:=k%11+2]*=1-(g[i-2][j]*g[i+2][j]*g[i][j-2]*g[i][j+2]<2)/4
 return[[(a,1+5*(a>1))[6in w+v]for*w,a in zip(*g,v)]for v in g]