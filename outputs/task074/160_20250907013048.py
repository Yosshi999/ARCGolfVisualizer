r=range(30)
m=lambda g,i,j:min(g[i][j],9*(j<2)+g[i][1-j],9*(i<2)+g[1-i][j],9*(i<2 or j<2)+g[1-i][1-j])
p=lambda g:[[min(m(g,i,j),m(g,j,i))for j in r]for i in r]