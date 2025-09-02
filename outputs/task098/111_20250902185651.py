e=enumerate
p=lambda g:[[a*(sum(v[j-(j>0):j+2]+w[i-(i>0):i+2])<6*a)for j,(*w,a)in e(zip(*g,v))]for i,v in e(g)]