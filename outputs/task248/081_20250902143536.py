def p(g):
 i=j=0
 for v in g[::-1]:v[i]=1;i+=(1,-1)[j//~-len(v)%2];j+=1
 return g