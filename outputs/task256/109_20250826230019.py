def p(g):
 i=g.index(v:=max(g));s=sum(v)//2
 for j in range(i+s):k=s+i-j;g[j][:k]=[(j<i)-(j>i)+2]*k
 return g