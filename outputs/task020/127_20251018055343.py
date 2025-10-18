f=lambda g:g.index(max(g,key=any))
p=lambda g,k=0:exec("n=f([*zip(*g)]);g[k%6+f(g)][k%5+n]|=g[f(g)+4-k%5][k%6+n];k+=1;"*73)or g