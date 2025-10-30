r=range(8)
p=lambda g:[[max(w[i],min(w[i%3::6]),min(g[i][j%3::6]))for*w,j in zip(*g,r)]for i in r]