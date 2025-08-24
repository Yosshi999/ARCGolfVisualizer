e=enumerate
d=lambda v,j:(v+[5]).index(5,j)+(v[::-1]+[5]).index(5,11-j)
p=lambda g:[[(5,0,6,7,8)[d(v,j)-11]if d(v,j)==d([*w],i)<16else 0for j,w in e(zip(*g))]for i,v in e(g)]