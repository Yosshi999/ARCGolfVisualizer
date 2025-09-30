r=range(-2,3)
R=range(10)
def p(g):h=eval(str(g));[h[i+y].__setitem__(j+1+x,g[i][j+(y*y==x*x)])for i in R for j in R for y in r for x in r if(x**3*y==y**3*x)*min(g[i][j:j+3])];return h