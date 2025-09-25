A=4+24;B=A+4+16;C=B+4+20;S=C
p=lambda g,n=S:n and p([[(
 (c,c+1)[d>0<c],
 (c,2)[(d&2==2)*(c>0)],
 (c,c+1)[(d==0<c)*(n%2)*(c>4)],
 (c,4)[(c&5==5)*(d==4)],
 (c,1)[c in[4,6]],
 (c,6)[(c>0)*(not(d in[0,1,2]))]
 )[(n<S-4+1)+(n<S-A+1)+(n<S-A-4+1)+(n<S-B+1)+(n<S-B-4+1)]
for c,d in zip(v,(0,)+v)]for v in zip(*g)][::-1],n-1)or g