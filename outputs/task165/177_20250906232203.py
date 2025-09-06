def p(g):
 G=sum(g,[]);C=max(c for x,c in enumerate(G)if G[x:x+2]+G[x+3:x+5]==[c]*4)
 return[*zip(*(C in v and v[:(b:=-v[::-1].index(C))]+20*[max(v[b:])]or v for*v,in zip(*g)))]