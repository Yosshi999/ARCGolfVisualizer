r=range(6)
p=lambda g,d=4:d and p([*zip(*(g[0][2]==g[2][0]==8)and[[g[i>2][j>2]*g[i+3][j+3]/3for j in r]for i in r]or g)][::-1],d-1)or g