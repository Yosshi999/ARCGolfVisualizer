f=lambda g:g.index(max(g,key=any))
p=lambda g,k=0:exec("m=f(g);n=f([*zip(*g)]);k%=25;g[k//5+m][k%5+n]|=g[m+4-k//5][k%5+n]|g[k%5+m][k//5+n];k+=1;"*50)or g