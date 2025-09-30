def p(g):
 I,J,H,s=[(i,j,h,s)for s in[4,3]for i in range(len(g))for j in range(len(g[0]))if all(H:=sum(h:=[v[j:j+s]for v in g[i:i+s]],[]))*len({*H})>1][0]
 for v in g[I:I+s]:v[J:J+s]=[0]*s
 q=[*eval('zip(*filter(max,'*2+'g))))')];d=len(q)//s;return[[a*(b>0)for a,b in zip(v,w[::d])]for v,w in zip(H,q[::d])]