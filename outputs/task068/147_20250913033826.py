e=enumerate
p=lambda g:[[(c:=min(h:=sum(g,[]),key=h.count),2)[w!=c]*any(c in u[j-(j>0):j+2]for u in g[i-(i>0):i+2])for j,w in e(v)]for i,v in e(g)]