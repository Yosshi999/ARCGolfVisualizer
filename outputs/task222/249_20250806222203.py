r=range(16)
def p(g):
 I,J,K,L=max([(i,j,k,l)for i in r for j in r for k in r for l in r if(i<k)*(j<l)],key=lambda t:(min(h:=sum([v[t[1]:t[3]]for v in g[t[0]:t[2]]],[]))>0,len({*h})<2,len(h)))
 return[[g[i][j]*(I<=i<K)*(J<=j<L)for j in r]for i in r]