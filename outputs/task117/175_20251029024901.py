e=enumerate
def p(g):
 for H in[(i,j)for i,v in e(g[2:])for j,w in e(v[2:])if{w,v[j],*g[i][j:j+3:2]}<{0,w}][-1]:g=[[w|(v+v)[2*H+2-j]for j,w in e(v)]for v in zip(*g)]
 return g