def p(g):
 for x in range(1728):
  i,j,d=x//144,x//12%12,x%12
  for v in g[i+1:i+d]*all(v[j:j+d+1]==[5,*[5-5*(0<y<d)]*~-d,5]for y,v in enumerate(g[i:i+d+1])):v[j+1:j+d]=[2]*~-d
 return g