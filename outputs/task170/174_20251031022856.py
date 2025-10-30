f=filter
def p(g):z=*h,u=[*f(any,g)];c,*w=f(int,u);r=range(s:=1+len(w));*q,=f(any,zip(*z[:-s]));d=len(q)//s;return[[z[i-s][u.index(c)+j]*(q[d*j][d*i]>0)for j in r]for i in r]