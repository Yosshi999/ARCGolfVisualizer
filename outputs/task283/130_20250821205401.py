e=enumerate
p=lambda g:[[g[i][j]and(1,4,2)[sum(v[max(j-1,0):j+2]+[*w[max(i-1,0):i+2]])//5-4]for j,w in e(zip(*g))]for i,v in e(g)]