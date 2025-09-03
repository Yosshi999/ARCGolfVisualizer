r=range(12)
def p(g):
 for i,j,d in[(i,j,d)for i in r for j in r for d in r[3:]if all(v[j:j+d]==[5,*[5-5*(i<y<i+d-1)]*(d-2),5]for y,v in enumerate(g[i:i+d],i))]:
  for v in g[i+1:i+d-1]:v[j+1:j+d-1]=[2]*(d-2)
 return g