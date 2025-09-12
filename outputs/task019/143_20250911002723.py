e=enumerate
def p(g):
 g=[v*2for v in g*2]
 for _ in[0]*4:g=[[w or(g[j-1][i-1]%8*i*j>0)*8for j,w in e(v)]for i,v in e(zip(*g))][::-1]
 return g