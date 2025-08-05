def p(g):
 exec('g+=g[0][:1]+g[-1][:-1],;'*(len(g[0])//2-1));
 return g