def p(g):
 h=[[0]*len(v)for v in g]
 r=[[a*(a==2)for*w,a in zip(*g,v)if 2in w]for v in g if 2in v]
 k=sum(g,[]).index(3)
 i,j=divmod(k,len(g[0]))
 h[i][j:j+7:6]=h[i+6][j:j+7:6]=[3]*2
 for x in range(5):h[i+x+1][j+1:j+6]=r[x]
 return h