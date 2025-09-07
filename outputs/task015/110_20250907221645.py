r=range(9)
p=lambda g,d=4:d and p([[g[~j][i]or(g[-j][i]==1)*7+4*(g[-j][i-1]==2)for j in r]for i in r],d-1)or g