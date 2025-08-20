def p(g):
 i=g.index(v:=max(g));s=sum(v)//2
 for j in range(i):k=s+i-j;g[j][:k]=[3]*k
 for j in range(s):g[i+s-j][:j]=[1]*j
 return g