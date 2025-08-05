def p(g):
 h=len(g);w=len(g[0])
 return[[((h-i-1-j)%(2*~-w)*((h-1-i+j)%(2*~-w))<1)*1for j in range(w)]for i in range(h)]