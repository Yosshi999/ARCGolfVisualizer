def p(g):
 t=5*len({*g[0]}-{0})-1;g[0]+=[0]*(t-4)
 exec('g[:0]=[[0]+g[0][:t]];'*t)
 return g