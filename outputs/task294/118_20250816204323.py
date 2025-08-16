e=enumerate
p=lambda g:[[2if v[j-1:j+2]==[5,5,5]and w[i-1:i+2]==(5,5,5)else v[j]for j,w in e(zip(*g))]for i,v in e(g)]