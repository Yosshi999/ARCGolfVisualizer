e=enumerate
p=lambda g,d=2:d and p([[x*((v[j-(j>0):j+2]+w[i-(i>0):i+2]).count(x)>3<sum(g,g).count(x)-1)for j,(*w,x)in e(zip(*g,v))]for i,v in e(g)],d-1)or g