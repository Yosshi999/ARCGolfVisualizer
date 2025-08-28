def p(g):
 *w,a,b=g;i=a.index(b[0])
 for j in range(i):v=w[-i+j];v[j]=v[~j]=b[i]
 return g