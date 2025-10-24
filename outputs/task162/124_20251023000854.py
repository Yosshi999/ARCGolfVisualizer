def p(g,k=0):
 j=k%18;h=g[k//18:][:3]
 for u in h*all(~-any(u[j:j+3])for u in h):u[j:j+3]=[1]*3
 return g*(k>323)or p(g,k+1)