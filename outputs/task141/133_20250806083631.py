e=enumerate
def p(g):h=sum(g,[]);k=h.index(m:=max(h));l=len(g[0]);return[[m*(abs(k//l-i)==abs(k%l-j))for j,w in e(v)]for i,v in e(g)]