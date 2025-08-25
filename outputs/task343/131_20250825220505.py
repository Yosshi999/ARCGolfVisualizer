def p(g):
 g=[*zip(*g)]
 if g[:3]==g[3:6]:g=g[:3]*5
 elif g[:3]==g[3:6][::-1]:g=g[:6]*2+g[:3]
 else:g=g[:8]+g[:7]
 return[*zip(*g)]