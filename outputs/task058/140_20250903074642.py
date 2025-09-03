r=range
def p(g):
 n=len(g);R=r(n);g=[[[3,0][min(x,n-x-1,y,n-y-1)%2]for x in R]for y in R]
 for k in r(n//2-(n%4==2)):g[k+1][k]^=3
 return g