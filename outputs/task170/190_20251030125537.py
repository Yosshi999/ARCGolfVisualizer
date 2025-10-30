f=filter
def p(g):*h,u=f(any,g);I=g.index(u);c,*w=f(int,u);J=u.index(c);r=range(s:=1+len(w));*q,=f(any,zip(*h[:1-s]));d=len(q)//s;return[[g[I-s-~i][J+j]*(q[d*j][d*i]>0)for j in r]for i in r]