def p(g):
 h=[*map(sum(g,[]).count,range(1,10))]
 l=[c for c in range(10)if sum(g,[]).count(c)==max(h)]
 l.sort(key=lambda x:sum(g,[]).index(x)%10)
 return[l]*max(h)