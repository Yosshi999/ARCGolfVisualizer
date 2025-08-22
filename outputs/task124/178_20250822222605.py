def p(g):
 if g[:2]*2==g[:4]:return g[:2]*5
 if g[:3]*2==g[:6]:return(g[:3]*4)[:10]
 m=sum(v>0for v in map(max,g[0],g[1]))-1
 return[([0]*(i//2)*m+g[i%2])[:10]for i in range(10)]