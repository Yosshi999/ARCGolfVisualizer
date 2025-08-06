r=range(16)
def p(g):
 _,I,J,K,L=max((len(h),i,j,k,l)for i in r for j in r for k in r for l in r if(0not in(h:=sum([v[j:l]for v in g[i:k]],[])))==len({*h}))
 return[[g[i][j]*(I<=i<K)*(J<=j<L)for j in r]for i in r]