def p(m):
 e=sorted((u:=sum(m,[])),key=u.count)[:2];b=[]
 for p,n in enumerate(m+[*zip(*m)]):
  for _,u in enumerate(n):
   if u in e:
    if len({*n})==2:d=n;t=sum(e)-u,u
    if p<len(m):b+=p+_,p-_-len(m)
 return[[{p+_,p-_-len(m)}&{*b}and t[u in d]or u for _,u in enumerate(n)]for p,n in enumerate(m)]