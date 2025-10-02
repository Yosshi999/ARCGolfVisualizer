f=lambda g:g.index(max(g,key=any))
p=lambda g,k=0:exec("m=f(g);n=f([*zip(*g)]);g[k%6+m][k%5+n]|=g[m+4-k%6][k%5+n]|g[k%5+m][k%6+n];k+=1;"*90)or g