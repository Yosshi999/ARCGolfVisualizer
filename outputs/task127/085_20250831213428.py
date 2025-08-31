e=enumerate
p=lambda g:[[(5,g[i&~3|1][j&~3|1]+5)[w<5]for j,w in e(v)]for i,v in e(g)]