def p(g):
 g=[*map(list,zip(*g))]
 for i in range(len(g)):g[i]=sorted(g[i],key=lambda x:x==0)
 return[*map(list,zip(*g))]