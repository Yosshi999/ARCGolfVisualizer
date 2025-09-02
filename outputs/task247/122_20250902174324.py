def p(g):
 d={};f=sum(zip(*g),())
 for v in f:d[v]=d.get(v,0)+(v>0)
 m=max(d.values());return[[c for c in d if d[c]==m]]*m