r=range(12)
def p(g):
 L=[(i,j,d)for i in r for j in r for d in r[3:]if max(i,j)+d<13 and g[i][j:j+d]==g[i+d-1][j:j+d]==[5]*d and all(v[j:j+d]==[5,*[0]*(d-2),5]for v in g[i+1:i+d-1])]
 for i,j,d in L:
  for v in g[i+1:i+d-1]:v[j+1:j+d-1]=[2]*(d-2)
 return g