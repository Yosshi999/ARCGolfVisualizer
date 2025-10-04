e=enumerate
def p(g):I=g.index(min(g),1);f=sum(sum(g[:I],[]))<sum(sum(g[I:],[]));return[[v[j]-(sum(v[j-1:j+2]+w[i-1:i+2])==24)*((3-f,2+f)[i<I])for j,(*w,)in e(zip(*g))]for i,v in e(g)]