f=lambda g:g.index(max(g,key=any))
p=lambda g:exec("m=f(g);n=f([*zip(*g)])\nfor i in range(m,m+5):\n for j in range(n,n+5):g[i][j]|=g[2*m+4-i][j]|g[j-n+m][i-m+n]\n"*2)or g