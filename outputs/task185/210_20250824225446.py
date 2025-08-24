def p(g):
 c=max(range(1,10),key=sum(g,[]).count)
 g=[[a*(a!=c)for*w,a in zip(*g,v)if{*w}-{0,c}]for v in g if{*v}-{0,c}]
 r=[0,1,2]
 return[[g[i][j]*(len(set(g[i][j:j+2]+g[i+1][j:j+2]))<2)for j in r]for i in r]