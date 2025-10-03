def p(g):
 b=max(G:=sum(g,[]),key=G.count);d={}
 for c in G:L=[i for i,v in enumerate(G)if b!=c==v];d|={i-sum(L)//4:c for i in L}
 w=len(g[0]);l=max(d)//w;r=range(-l,l+1);return[[d.get(i*w+j,b)for j in r]for i in r]