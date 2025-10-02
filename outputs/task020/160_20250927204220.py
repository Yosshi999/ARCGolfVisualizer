r=range(5)
f=lambda g:g.index(max(g,key=any))
p=lambda g:exec("m=f(g);n=f([*zip(*g)])\nfor i in r:\n for j in r:g[i+m][j+n]|=g[m+4-i][j+n]|g[j+m][i+n]\n"*2)or g