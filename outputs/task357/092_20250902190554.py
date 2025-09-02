def p(g):
 i=j=0
 for v in g[::-1]:l=len(v);v[:]=[8]*l;v[i]=1;i+=1-j//~-l%2*2;j+=1
 return g