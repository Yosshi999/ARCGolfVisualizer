e=enumerate
p=lambda g:[[v[j]-sum(v[j-1:j+2]+w[i-1:i+2])//30*3for j,(*w,)in e(zip(*g))]for i,v in e(g)]