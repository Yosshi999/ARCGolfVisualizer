r=range(10)
p=lambda g,d=96:d and p([[g[j-1][i-1]*(g[j-2][i-2]>g[j-1][i-2]<i>1<j)or g[j][i]for j in r]for i in r][::-1],d-1)or g