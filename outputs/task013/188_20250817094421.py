t=lambda g:[*map(list,zip(*g))]
def p(g):g=(g,t(g))[f:=g[0]==g[-1]];h=[*map(max,*g)];a,b=[i for i,v in enumerate(h)if v];g=[(h[:a]+(h[a:b+1]+h[a+1:b])*9)[:len(h)]]*len(g);return(g,t(g))[f]