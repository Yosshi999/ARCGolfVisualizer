e=enumerate
p=lambda g:[[2*(sum(v[j-1:j+2]+[*w[i-1:i+2]])==30)or v[j]for j,w in e(zip(*g))]for i,v in e(g)]