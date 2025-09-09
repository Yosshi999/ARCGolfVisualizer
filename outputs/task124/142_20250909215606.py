def p(g):
 if g[:3]*2==g[:6]:return(g[:3]*4)[:10]
 m=2-(g[0][:9]==g[2][1:])-2*(g[0]==g[2])
 return[(i//2*m*[0]+g[i%2])[:10]for i in range(10)]