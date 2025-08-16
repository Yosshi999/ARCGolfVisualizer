e=enumerate
p=lambda g:[[2if sum(v[j-1:j+2]+[*w[i-1:i+2]])==30else v[j]for j,w in e(zip(*g))]for i,v in e(g)]