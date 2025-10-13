def p(g):
 I=g.index(u:=max(g[::-1],key=any));J=u.index(max(u,key=bool));s=3+(u[J+3]>0);H=[]
 for v in g[I-s+1:I+1]:H+=v[J:J+s],;v[J:J+s]=[0]*s
 q=[*eval('zip(*filter(max,'*2+'g))))')];d=len(q)//s;return[[a*(b>0)for a,b in zip(v,w[::d])]for v,w in zip(H,q[::d])]