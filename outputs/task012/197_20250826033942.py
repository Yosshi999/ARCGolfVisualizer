R=range(-2,3)
E=enumerate
def p(g):k=[*map(list,g)];[k[i+y].__setitem__(j+x,[v[j-1],w][y*y==x*x])for i,v in E(g)for j,w in E(v)for y in R for x in R if w and(x**3*y==y**3*x)*v[j-1]*v[j+1]];return k