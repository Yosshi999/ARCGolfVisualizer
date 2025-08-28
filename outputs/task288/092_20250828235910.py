def p(g):
 *_,a,b=g;i=a.index(b[0])
 for j in range(i):v=g[-i-2+j];v[j]=v[~j]=b[i]
 return g