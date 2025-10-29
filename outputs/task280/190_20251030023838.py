e=enumerate
p=lambda g,d=4:d and p([max([v]+[((k!=i)+2,)*l+v[l:]for k,u in e(zip(*g))for l,_ in e(u)if abs(k-i)<[*u[l:],0].index(0)*((0,2)==u[l-1:l+1])])for i,v in e(zip(*g))][::-1],d-1)or g