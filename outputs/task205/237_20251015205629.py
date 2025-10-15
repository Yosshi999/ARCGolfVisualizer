def p(g,d=0):
 c=max(v:=sum(g,g),key=v.count)
 n=max(v.count(c)for v in zip(*g))
 g=[[*v]for v in zip(*g)if v.count(c)>n*d-2]
 if d<1:return p(g,d+.1)
 C=min(v:=sum(g,[]),key=v.count)
 return[[(c,C)[C in v+w]for*w,in zip(*g)] for v in g]