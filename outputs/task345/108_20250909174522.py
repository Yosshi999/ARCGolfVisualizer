def p(g):
 for v,w in zip(g[::-1],g[8::-1]):j=0;exec('if v[j]&2:v[k:=j+w[j]%2]=w[k]=2\nj+=1\n'*10)
 return g