def p(g):
 f=sum(g,[])
 c=max({*f}-{0},key=f.count)
 g=[[a for*w,a in zip(*g,v)if{*w}-{0,c}]for v in g if{*v}-{0,c}]
 r=[0,1,2]
 #return g
 return[[g[i][j:j+2]+g[i+1][j:j+2]==[g[i][j]]*4 and g[i][j]*(g[i][j]!=c)for j in r]for i in r]