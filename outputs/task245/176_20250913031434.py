def p(g):
 h=eval(str(g).replace(*'20'));u=max(h);j=u.index(3)
 for x in range(5):h[h.index(u)+x+1][j+1:j+6]=[[a%3for*w,a in zip(*g,v)if 2in w]for v in g if 2in v][x]
 return h