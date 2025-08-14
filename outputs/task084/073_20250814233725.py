def p(g):
 c=1
 exec('g[-1][c]=4;g[~c][c]=2;c+=1;'*~-len(g[0]))
 return g