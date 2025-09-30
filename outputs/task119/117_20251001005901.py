r=range(12)
p=lambda g:exec('g[::-1]=[[g[j][i]or(g[j-1][i-1]*g[j-2][i-2]>4>0<i>1<j)*3for j in r]for i in r];'*40)or g